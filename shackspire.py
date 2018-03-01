from bs4 import BeautifulSoup
import urllib.request
import nltk
import re

#nltk.download('words')

#page with the text "Othello" Shakespeare
r = urllib.request.urlopen(
					'http://shakespeare.mit.edu/othello/full.html')
doc = r.read().decode('utf-8')

#get text "Othello"
soup = BeautifulSoup(doc, 'html.parser')
text = soup.get_text()

#separate text into tokens
tokens = nltk.tokenize.word_tokenize(text)

main_dict = {}
other_list = set()
#the most common words of our time
all_words = nltk.corpus.words.words()

#take a list of some words without punctuation marks, etc.
list_of_text = [word.lower() for word in tokens if word.isalpha()]

#fill the dictionary of words that are not used
for word in list_of_text:
	if word in main_dict:
		main_dict[word] = main_dict[word] + 1
	else:
		if (word not in other_list) and (word not in all_words):
			main_dict[word] = 1
		else:
			other_list.add(word)
			
count = 1
#output 25 frequent words that are not used in the text
for word in sorted(main_dict, key=main_dict.get, reverse=True):
	if count == 26:
		break
	print(word.capitalize())
	count += 1


			
	
