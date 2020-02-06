##Stemmer
import string
SUFFIXES = ("ing", "ed", "s")

def countWords(text):
    translation = text.maketrans("", "", string.punctuation.replace("'", ""))
    text = text.translate(translation).lower()

    words = text.split()
    dict = {}
    for word in words:
        if not word in dict:
            dict[word] = 1
        else:
            dict[word] += 1

    dict = {k: v for k, v in sorted(dict.items(),
        key = lambda item: item[1], reverse = True)}

    return dict

def stem(word):
    stemmed = word
    for suffix in SUFFIXES:
        #is this hacky?
        if word.endswith(suffix) and not word[:-len(suffix)].endswith(suffix):
            stemmed = word[:-len(suffix)]
        while stemmed.endswith('i') or stemmed.endswith('e'):
            if stemmed.endswith('i'): stemmed = stemmed[:-1]+'y'
            else: stemmed = stemmed[:-1]
    return stemmed
