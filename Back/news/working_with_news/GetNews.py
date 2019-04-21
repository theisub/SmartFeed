import requests
import newspaper
from newspaper import Article
from newspaper.network import multithread_request
import xml.etree.ElementTree as ET
import json
import re
from GetFeed import SortNewsByInterest,FormUserFeed
from multiprocessing.dummy import Pool as ThreadPool
import time 

def GetTxt(url,language ='ru'):
    """
    Парсер новостей для формирования новости в виде JSON.
    
    @type url: str
    @param url: URL-адрес новости

    @type language: str
    @param language: Язык новости для правильной обработки (по умолчанию русский) 

    @rtype: str|dict
    @return: Возвращает новость со следующими полями: изображение, url-адрес новости, заголовок, текст новости, краткое описание новости
    """
    
    article = Article(url['url'],language= language)
    article.download()
    try:
        data = dict()
        article.parse()
        data['tag'] = url['tag']
        data['coef'] = url['coef']
        data['img'] = article.top_img
        data['url'] = article.url
        data['title'] = article.title
        data['text']=article.text
        if article.meta_description == '':
            data['description'] = re.sub(r'[-^@#$«»\n/]', "",  article.text)[:80]
        else:
            data['description'] = article.meta_description 

        return data
    except:
        return ""

def GetResponses(tag,limit = 'nolimit'):
    """
    Получение URL-адресов новостей по указанному тегу. Происходит обращение к RSS от Google News. 
    
    @type tag: str
    @param tag: Тег по которому производится поиск новостей

    @type limit: str|int
    @param limit: Предел количества выводимых адресов новостей (по умолчанию без ограничения)

    @rtype: list
    @return: Возвращает список URL-адресов новостей 
    """

    request = ('https://news.google.com/rss/search?q=%s&num=5&hl=ru&gl=RU&ceid=RU:ru' % (tag))
    response = requests.get(request, stream=True)
    response.raw.decode_content = True
    text = response.text
    content = response.content
    all_urls = []
    data =ET.fromstring(text)
    test = data.findall('./channel/item/link')
    if limit == 'nolimit':
        limit = len(test)
    else:
        limit = limit
    
    

    for child in test[0:limit]:
        all_urls.append(child.text)
    return all_urls


def get_news_feed(tags_for_feed, blocked_news):

    start = time.time()
    pool1 = ThreadPool(len(tags_for_feed))

    urls = pool1.map(GetResponses,tags_for_feed)
    pool1.close()
    pool1.join()

    #forming len

    end = time.time()
    print("get urls from rss", end - start)
    urls_to_parse =[]
   
    start = time.time()

    for i in range(len(urls)):
        res = [i for i in urls[i] if i not in blocked_news] 
        #res = urls[i].difference(blocked_news)
        if len(res) > 0:
            data = dict()
            data['tag'] = list(tags_for_feed.keys())[i]
            data['coef'] = list(tags_for_feed.values())[i]
            data['url'] = res[0]
            urls_to_parse.append(data)

    end = time.time()
    print("form non repeating dict", end - start)

    feedsize = 9

    start = time.time()
    pool2 = ThreadPool(feedsize)

    results = pool2.map(GetTxt,urls_to_parse)

    pool2.close()
    pool2.join()

    end = time.time()

    print("parsing news", end - start)
    SortNewsByInterest(results)
    results = FormUserFeed(results)

    return results

#пример который нужно будет перенести в views.py

#blocked_news = []
#tags_for_feed = {'Apple':0.6,"Samsung":0.5,"HTC":0.3,'Microsoft': 0.4,'Sony':0.7,'Nintendo':0.4,'Atari':0.3,'iOS':0.2,'Android':0.4,'Apple':0.6,"Samsung":0.5,"HTC":0.3,'Microsoft': 0.4,'Sony':0.7,'Nintendo':0.4,'Atari':0.3,'iOS':0.2,'Android':0.4,'Apple':0.6,"Samsung":0.5,"HTC":0.3,'Microsoft': 0.4,'Sony':0.7,'Nintendo':0.4,'Atari':0.3,'iOS':0.2,'Android':0.4,'Apple':0.6,"Samsung":0.5,"HTC":0.3,'Microsoft': 0.4,'Sony':0.7,'Nintendo':0.4,'Atari':0.3,'iOS':0.2,'Android':0.4,'Apple':0.6,"Samsung":0.5,"HTC":0.3,'Microsoft': 0.4,'Sony':0.7,'Nintendo':0.4,'Atari':0.3,'iOS':0.2,'Android':0.4,'Apple':0.6,"Samsung":0.5,"HTC":0.3,'Microsoft': 0.4,'Sony':0.7,'Nintendo':0.4,'Atari':0.3,'iOS':0.2,'Android':0.4,'Apple':0.6,"Samsung":0.5,"HTC":0.3,'Microsoft': 0.4,'Sony':0.7,'Nintendo':0.4,'Atari':0.3,'iOS':0.2,'Android':0.4,'Apple':0.6,"Samsung":0.5,"HTC":0.3,'Microsoft': 0.4,'Sony':0.7,'Nintendo':0.4,'Atari':0.3,'iOS':0.2,'Android':0.4,'Apple':0.6,"Samsung":0.5,"HTC":0.3,'Microsoft': 0.4,'Sony':0.7,'Nintendo':0.4,'Atari':0.3,'iOS':0.2,'Android':0.4,'Apple':0.6,"Samsung":0.5,"HTC":0.3,'Microsoft': 0.4,'Sony':0.7,'Nintendo':0.4,'Atari':0.3,'iOS':0.2,'Android':0.4}
#res = get_news_feed(tags_for_feed,blocked_news)

