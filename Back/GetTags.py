import pymorphy2
import re
import operator

def create_tags(text, n=5):
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
	
if __name__ == "__main__":
	f = open("text.txt", "r")
	text = f.read()
	f.close()

	print(create_tags(text))