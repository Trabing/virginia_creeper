from bs4 import BeautifulSoup
import requests
import nltk
import re
from ignore import words_to_ignore
from collections import Counter
from random import randint
import pickle

nltk.data.path.append("./nltk_data/")
sans_punctuation = re.compile(".*[A-Za-z].*")

response = requests.get("http://www.katabasis.org")
structured_text = BeautifulSoup(response.text, "html.parser").get_text()
unstructured_text = nltk.word_tokenize(structured_text)
restructured_text = nltk.Text(unstructured_text)
words = [word for word in restructured_text if sans_punctuation.match(word)]
words_frequency = Counter(words)
keywords = [word for word in words if word.lower() not in words_to_ignore]
keywords_frequency = Counter(keywords)

with open("newjar.pkl", "wb") as f:
        pickle.dump(keywords_frequency, f)

with open("newjar.pkl", "rb") as f:
        print(pickle.load(f))
