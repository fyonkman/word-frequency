##Stemmer
import string
import pickle
SUFFIXES = ("ing", "ed", "s")

def countWords(text, stopwords):
    translation = text.maketrans("", "", string.punctuation.replace("'", ""))
    text = text.translate(translation).lower()

    words = text.split()
    dict = {}

    if stopwords:
        with open("stopwordslist.txt", "rb") as file:
            stopwordslist = pickle.load(file)

        for word in words:
            if not word in stopwordslist:
                word=stem(word)
                if not word in dict:
                    dict[word] = 1
                else:
                    dict[word] += 1
    else:
        for word in words:
            word=stem(word)
            if not word in dict:
                dict[word] = 1
            else:
                dict[word] += 1

    dict = {k: v for k, v in sorted(dict.items(),
        key = lambda item: item[1], reverse = True)}

    dict = {k: dict[k] for k in list(dict.keys())[:25]}
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

if __name__=="__main__":
    print(countWords("yourselves asdflwqoeru asdf qwe tyre poiun", stopwords=1))
