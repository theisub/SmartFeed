import pymorphy2
import re
import operator

def create_tags(text, n):
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
	return sort[-n:]
	
if __name__ == "__main__":
	f = open("text.txt", "r")
	text = f.read()
	f.close()

	print(create_tags(text, 10))