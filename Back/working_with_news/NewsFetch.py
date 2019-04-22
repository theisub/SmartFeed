import requests
import newspaper
from newspaper import Article
from newspaper.network import multithread_request
import xml.etree.ElementTree as ET
import json
import re
from multiprocessing.dummy import Pool as ThreadPool
import time 
import random

def GetTxt(url,language ='ru'):
    """!
    Парсер новостей для формирования новости в виде JSON.
    
    @param str url: URL-адрес новости

    @param str language: Язык новости для правильной обработки (по умолчанию русский) 

    @return str|dict: Возвращает новость со следующими полями: изображение, url-адрес новости, заголовок, текст новости, краткое описание новости
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
            data['description'] = article.meta_description [:80]

        return data
    except:
        return ""

def GetResponses(tag,limit = 'nolimit'):
    """!
    Получение URL-адресов новостей по указанному тегу. Происходит обращение к RSS от Google News. 
    
    @param str tag: Тег по которому производится поиск новостей

    @param str|int limit: Предел количества выводимых адресов новостей (по умолчанию без ограничения)

    @return list: Возвращает список URL-адресов новостей 
    """

    request = ('https://news.google.com/rss/search?q=%s&num=5&hl=ru&gl=RU&ceid=RU:ru' % (tag[0]))
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