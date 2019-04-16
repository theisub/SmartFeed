import requests
import xml.etree.ElementTree as ET
import json



def GetResponses(tag,limit = 'nolimit'):
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

    