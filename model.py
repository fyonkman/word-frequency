##@Fiona Yonkman 2020
##Python file contains functions countWords and stem
import string
import pickle
SUFFIXES = ("ing", "ed", "s")

"""
Arguments: String text and stopwords (which is either None or "on")

Output: Dictionary of max length 25, keys are words in the text input, values
are their occurance in the text

Function: the countWords() function creates a word frequency dictionary based
on an inputted string of words. Words that are conjugated are grouped by stem.
If the stopwords box is checked, the most common words will not be included
in the returned dictionary.
"""
def countWords(text, stopwords):
    #remove all punctuation except apostrophes
    translation=text.maketrans("", "", string.punctuation.replace("'", ""))
    text=text.translate(translation).lower()

    words=text.split()
    dict={}

    #remove stopwords if selected, stem words, add words to dictionary
    if stopwords:
        with open("stopwordslist.txt", "rb") as file:
            stopwordslist=pickle.load(file)

        for word in words:
            if not word in stopwordslist:
                word=stem(word)
                if not word in dict:
                    dict[word]=1
                else:
                    dict[word]+=1
    else:
        for word in words:
            word=stem(word)
            if not word in dict:
                dict[word]=1
            else:
                dict[word]+=1

    #sort dictionary by highest frequency first, truncate dictionary at 25 words
    dict={k: v for k, v in sorted(dict.items(),
        key=lambda item: item[1], reverse = True)}

    dict={k: dict[k] for k in list(dict.keys())[:25]}
    return dict

"""
Argument: String word

Output: String word which is stem of input

Function: the stem() function takes a word as input and returns itself if it is
already the stem, or the stemmed version if it is conjugated. This works with
the test words and conjugated forms: "talk, copy, pass, play"
"""
def stem(word):
    stemmed=word
    for suffix in SUFFIXES:
        if word.endswith(suffix) and not word[:-len(suffix)].endswith(suffix):
            stemmed=word[:-len(suffix)]
            while stemmed.endswith('i') or stemmed.endswith('e'):
                if stemmed.endswith('i'): stemmed = stemmed[:-1]+'y'
                else: stemmed=stemmed[:-1]
    return stemmed

if __name__=="__main__":
    print(countWords("yourselves asdflwqoeru asdf qwe tyre poiun", stopwords=1))
