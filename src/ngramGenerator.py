
# code for N-gram generator based on nltk module
# K-most frequent words in a class of tweets
import nltk
import operator # for sorting dictionnares
import sys
# to suppress warning - https://stackoverflow.com/questions/14463277/how-to-disable-python-warnings
import warnings
if not sys.warnoptions:
    warnings.simplefilter("ignore")
# getting word frequencies from training data for a given class

def getTweetWords(tweet):
    all_words = []
    sTweet=tweet.split()
    return sTweet

def get_word_features(wordlist): 
    wordlist = nltk.FreqDist(wordlist)
    result=[]
    for k in wordlist.keys():
        result.append([k,wordlist[k]])
    return result

def ngramText(filename): # generate vector of ngrams in text file
    textWords=[]
    f=open(filename,"r")
    line=f.readline()
    while line:
        textWords.extend(getTweetWords(line))
        line=f.readline()
    f.close()
    return textWords

def sortList(x):
    return list(reversed(sorted(x, key=operator.itemgetter(1))))

def mostFreqList(filename,k): # extract k most frequent words from the sorted list
    d=get_word_features(ngramText(filename))
    l=sortList(d)
    m=[w[0] for w in l[0:k]]
    return m


filename="../data/positive_processed.csv"
#ngram=ngramText(filename)

#print get_words_in_tweets(tweets)
#print mostFreqList(filename,5)
#word_features = get_word_features(get_words_in_tweets(tweets))
