import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import nltk

text = 'Cats are chasing mice in the garden'
words = word_tokenize(text)
lemmatize = WordNetLemmatizer()


def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('v'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN


lemmatized_words = []
for word, pos in nltk.pos_tag(words):
    wordnet_get = get_wordnet_pos(pos)
    lemma = lemmatize.lemmatize(word, wordnet_get)
    lemmatized_words.append(lemma)

print(lemmatized_words)
