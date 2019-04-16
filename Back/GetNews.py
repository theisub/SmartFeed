import requests
import newspaper
from newspaper import Article
from newspaper.network import multithread_request
import xml.etree.ElementTree as ET
import json
#TODO:Обработка ошибок

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
    article = Article(url,language= language)
    article.download()
    try:
        data = dict()
        article.parse()
        data['img'] = article.top_img
        data['url'] = article.url
        data['title'] = article.title
        data['text']=article.text
        data['description'] = article.meta_description # TODO: Адекватно сократить исходное тело новости до краткой аннотации
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
