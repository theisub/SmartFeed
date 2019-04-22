import pymorphy2
import re
import operator
from newspaper import Article

def create_tags(text, n=5):
    """!
    Создание списка тегов для заданного текста
    
    @param str text: Текст, заданный строкой

    @return list: Возвращает список, состоящий из списков, содержащих теги и их коэффициенты
    """
	text = re.sub(r'[-—.,:^!?@#$%()"«»\n]', "", text) 
	text = re.sub(r'  ', " ", text)
	words = re.split(r' ', text)

	morphAnal = pymorphy2.MorphAnalyzer()

	bad_words = ["PREP", "CONJ", "PRCL", "ADJF", "NPRO", "VERB", "ADVB"]

	count = {}
	for word in words:
		word_morph = morphAnal.parse(word)
		
		tag = word_morph[0].tag
		
		flag = True
		for b in bad_words:
			if b in tag:
				flag = False

		if flag:
			norm = word_morph[0].normal_form
			temp = count.get(norm, 0)
			count[norm] =  temp + 1

	count.pop('', 0)

	sort = sorted(count.items(), key = operator.itemgetter(1))
	sort = sort[-n:]
	
	count_tags = 0
	for cur in sort:
		count_tags = count_tags + cur[1]
		
	list_sort = []		
	for cur in sort:	
		list_cur = [cur[0], cur[1]/count_tags]
		list_sort.append(list_cur)
		
		
	return list_sort
	
#user_tags - словарь
def update1(user_tags, article_tags):
    """!
    Обновление коэффициентов пользователя
    
    @param dict user_tags: Старые теги пользователя
	@param list article_tags: Теги из статьи

    @return dict: Новые коэффициенты
    """
	k = 1 # коэффициент
		
	for tag in article_tags:
		temp = user_tags.get(tag[0], 0)
		user_tags[tag[0]] = temp + (1-temp)*k*tag[1]
	return user_tags
	
def GetTxt(url): 
    """!
    Получение текста статьи по её URL
    
    @param str url: URL статьи

    @return str: Текст статьи
    """
    article = Article(url) 
    article.download() 
    try: 
        article.parse() 
        data = article.text 
        return data 
    except: 
        return ""
		
def update_tags(url, old_tags):
    """!
    Обновление коэффициентов пользователя
    
    @param str url: URL статьи
    @param dict old_tags: Старые теги пользователя
	
	
    @param dict user_tags: Новые теги пользователя
    """
	text=GetTxt(url)
	article_tags = create_tags(text)
	new_tags = update1(old_tags, article_tags)
	return new_tags


	
if __name__ == "__main__":
	f = open("text.txt", "r")
	text = f.read()
	f.close()
	current_tags = create_tags(text)
	print(current_tags)
	
	user_tags = {'словарь':0.1, 'язык':0.2, 'слово':0.5}
	print(user_tags)
	for i in range(6):	
		user_tags = update1(user_tags, current_tags)
		print(user_tags)
