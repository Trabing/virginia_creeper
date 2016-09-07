import os
from bs4 import BeautifulSoup
import requests
import nltk
import re
import operator
from flask import Flask, render_template, request
from ignore import words_to_ignore
from collections import Counter
from random import randint
import pickle


app = Flask(__name__)
app.config.from_object(os.environ["APP_SETTINGS"])

@app.route("/")
def index():
        return render_template("index.html")

@app.route("/seek", methods=["GET","POST"])
def seek():
        errors = []
        results = {}
        if request.method == "POST":
                try:
                        url = request.form["url"]
                        if "http://" not in url[:7]:
                                url = "http://" + url
                        response = requests.get(url)
                except:
                        errors.append(
                                "Invalid URL."
                        )
                        return render_template(
                                        "index.html",
                                        errors=errors
                        )
                if response:
                        nltk.data.path.append("./nltk_data/")
                        sans_punctuation = re.compile(".*[A-Za-z].*")
                        structured_text = BeautifulSoup(response.text, "html.parser").get_text()
                        unstructured_text = nltk.word_tokenize(structured_text)
                        restructured_text = nltk.Text(unstructured_text)
                        words = [word for word in restructured_text if sans_punctuation.match(word)]
                        words_frequency = Counter(words)
                        keywords = [word for word in words if word.lower() not in words_to_ignore]
                        keywords_frequency = Counter(keywords)
                        results = sorted(
                                keywords_frequency.items(),
                                key = operator.itemgetter(1),
                                reverse = True
                        )
        return render_template(
                        "index.html",
                        errors=errors,
                        results=results
        )

#with open("newjar.pkl", "wb") as f:
#        pickle.dump(keywords_frequency, f)

#with open("newjar.pkl", "rb") as f:
#        print(pickle.load(f))

if __name__ == "__main__":
        app.run(debug=True)
