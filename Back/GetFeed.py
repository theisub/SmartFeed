
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

