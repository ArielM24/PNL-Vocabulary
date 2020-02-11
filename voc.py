import nltk
from nltk.corpus import PlaintextCorpusReader
from bs4 import BeautifulSoup
import re

#Texto plano
f = open("corpus/e961024.htm", encoding = "utf-8")
text = f.read()
f.close()

#Limpiar etiquetas html
soup = BeautifulSoup(text,"lxml")
words = soup.get_text()
#print(words)


#tokens nltk
tokens_nltk = nltk.word_tokenize(words)
#print(tokens_nltk)

#tokens con split
#tokens_py = words.split()
#print(tokens_py)

#quitando stop words y signos de puntuacion
fsw = open("spanish_stop_words.txt","r")
stop_words = fsw.read()
fsw.close()

fsp = open("spanish_punctuation_signs.txt","r")
puntuacion_signs = fsp.read()
fsp.close()

vocabulary = []
for word in tokens_nltk:
	if(word not in stop_words and word not in puntuacion_signs):
		vocabulary.append(word)

#Rewrite de words in lowercase and sort
vocabulary = [word.lower() for word in vocabulary]
#vocabulary.sort()



#dividiendo cadenas con simbolos intermedios
sym = ["-","/","'","*","?","¿","!","¡",".",",",";",":","¦","#","&","%","$","(",")","=","_","[","]","{","}","~","+","—","\\"]
num = ["0","1","2","3","4","5","6","7","8","9"]
def erase_sym(str, sym):
	strings = []
	aux = []
	added = False
	for symbol in sym:
		f = str.find(symbol)
		if f > -1:
			strings = strings + str.split(symbol)
			added = True
			for s in strings:
				aux = aux + erase_sym(s,sym)
			return aux

	if not added:
		strings.append(str)

	return strings
	
def erase_size(str,size):
	aux = []
	for s in str:
		if len(s) > size:
			aux.append(s)
	return aux

tokens_normalizados = []
for word in vocabulary:
	tokens_normalizados = tokens_normalizados + erase_size(erase_sym(word,sym+num),1)

sorted_vocabulary = sorted(set(tokens_normalizados))
#print(len(sorted_vocabulary))

#Guardando vocabulario en un archivo

'''fv = open("tokens_normalizados.txt","w")
for word in tokens_normalizados:
	fv.write(word + "\n")
fv.close()'''

#print(sorted_vocabulary[0:100])

contexts = {}
window = 8

for i in range(len(tokens_normalizados)):
	for j in range(i - int(window/2)):
		try:
			if j >= 0:
				pass
		except IndexError:
			pass

