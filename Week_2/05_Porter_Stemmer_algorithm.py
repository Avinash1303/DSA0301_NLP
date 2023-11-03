import nltk
from nltk.stem import PorterStemmer

# Initialize the Porter Stemmer
stemmer = PorterStemmer()

# List of words to be stemmed
words = ["jumping", "jumps", "jumped", "jump",
         "flying", "flies", "fly", "running", "runs", "run"]

# Perform word stemming
stemmed_words = [stemmer.stem(word) for word in words]

# Print the original words and their stemmed forms
for original, stemmed in zip(words, stemmed_words):
    print(f"{original} -> {stemmed}")
