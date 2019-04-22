
def SortNewsByInterest(news):
    """!
    Сортировка ленты новостей по коэффициенту интересности
    
    @param list news: Лента новостей

    @return dict: Возвращает ленту новостей отсортированной по полю 'coef'
    """
    news.sort(key=lambda x: x['coef'], reverse=True)
    return news

def FormUserFeed(news):
    """!
    Формирование сокращенной ленты пользователя 
    
    @param list news: Лента новостей

    @return dict: Возвращает сокращенную ленту новостей, которые состоят из полей изображения, URL, заголовка и краткого описания 
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

