
def SortNewsByInterest(news):
    """
    Сортировка ленты новостей по коэффициенту интересности
    
    @type news: list
    @param news: Лента новостей

    @rtype: list
    @return: Возвращает ленту новостей отсортированной по полю 'coef'
    """
    news.sort(key=lambda x: x['coef'], reverse=True)
    return news

def FormUserFeed(news):
    """
    Формирование сокращенной ленты пользователя 
    
    @type news: list
    @param news: Лента новостей

    @rtype: dict
    @return: Возвращает сокращенную ленту новостей, которые состоят из полей изображения, URL, заголовка и краткого описания 
    """
    feedkeys = ['img','url','title','description']
    shortfeed = []
    for article in news:
        shortfeed.append({key:article[key] for key in feedkeys})

    editedfeed = {
        'size': len(shortfeed),
        'articles' : shortfeed
    }

    return editedfeed

