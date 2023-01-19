import numpy as np
import nltk
from nltk.stem.porter import PorterStemmer
# should know all these module

Stemmer = PorterStemmer()

def tokenize(sentence):                #tokenize/ break sentences or data and find pattern on different sentence
    return nltk.wordpunct_tokenize(sentence)

def stem(word):                         # reduce the redundency for same type of words, for efficient searching
    return Stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence,words):
    sentence_word = [stem(word) for word in tokenized_sentence]
    bag = np.zeros(len(words),dtype = np.float32)

    for idx , w in enumerate(words):
        if w in sentence_word:
            bag[idx] = 1
    return bag