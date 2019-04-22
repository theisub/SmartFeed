import requests
import newspaper
from newspaper import Article
from newspaper.network import multithread_request
import xml.etree.ElementTree as ET
import json
import re
from working_with_news.GetFeed import SortNewsByInterest,FormUserFeed
from working_with_news.NewsFetch import GetResponses,GetTxt
from multiprocessing.dummy import Pool as ThreadPool
import time 
import random

def get_news_feed(tags_for_feed, blocked_news):
 
    high_tier = []
    low_tier = []

    feedsize = 9
    tags_for_feed = list(tags_for_feed.items())
    random.shuffle(tags_for_feed)
    tags_for_feed = tags_for_feed[:feedsize]
    mean = sum(x[1] for x in tags_for_feed)/len(tags_for_feed)
    if len(tags_for_feed) >= feedsize:
        for item in tags_for_feed:
            if item[1] > mean:
                high_tier.append(item)
            else:
                low_tier.append(item)
    elif len(tags_for_feed) > 0:
        while len(high_tier) < feedsize:
            high_tier.append(tags_for_feed[random.randint(0,len(tags_for_feed)-1)])
    else:
        return


    random.shuffle(low_tier)
    random.shuffle(high_tier)

    tags_for_feed = high_tier + low_tier  
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
        if len(res) > 0:
            data = dict()
            data['tag'] = (tags_for_feed[i])[0]
            data['coef'] = (tags_for_feed[i])[1]
            data['url'] = res[0]
            blocked_news.append(res[0])
            urls_to_parse.append(data)

    end = time.time()
    print("form non repeating dict", end - start)


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
