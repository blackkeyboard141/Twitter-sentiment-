# Required imports or library dependencies
import re, sys, json
from tweet_sentiment import *
from matlibbbb import *


MAX_VALUE = 5

# Generate predicted Sentiment Dictionary from tweet score and unknown tweet terms.
# May want to use try except block
# The predSentDict updates automatically that is why we do not return anything.
# Fill the rest, details explained in class.
def genPredSentDict(score, numTerms, uTerms, predSentDict):#method 4 #score= full tweet score, numterms = number of all terms in tweet, uterms = unknown terms list, newsentdictionary is a new dictionary
    for uTerm in uTerms:
       if(uTerm in predSentDict):
                predSentDict[uTerm][0]=predSentDict[uTerm][0]+score
                predSentDict[uTerm][1] = predSentDict[uTerm][1] + numTerms
       else: predSentDict[uTerm] = [score, numTerms]
        

# Analyse The tweet
# Input: Tweet terms as list, and the sentiment dictionary - hashmap/map
# Output: tweet score, unknown terms as a set data structure.
# Fill the rest. 
# Details explained in class.
def tweetAnalysis(tweet_terms, sentDict, tweet):  #method 3 - tweet_terms has the list of english words of the tweet
    tweet_score = 0
    unknown_terms = set()
    known= set()
    tweet_score= getSentScoreOfTweet(tweet,sentDict)

    for term in tweet_terms: #check the term in the dictionary, if not present, give it the score of the whole tweet. where to get score of the whole tweet? use getSentScoreOfTweet
        if term in sentDict:
                known.add(term)
        else:
            unknown_terms.add(term)
    return tweet_score, unknown_terms #the output is the list of unknown terms and the combined tweetscore of that tweet


# Refine the new sentiment dicionary!
# Details explained in class.
# Update the new sentiment dictionary, therefore no explicit return
# Fill the rest.
def refinePredSentDict(newSentDict):#method 5
    for key in newSentDict.keys():
       newSentDict[key]=float(newSentDict[key][0])/float(newSentDict[key][1])*5




def printSentDict(sentDict):
    for key in sentDict.keys():
        value = sentDict[key]
        print("%s %.4f" % (key, value))


def initPredSentDict(sentDict, tweets_file): #method 2
    newSentDict = {}    
    tweets_file = open(tweets_file)
    sentDict = genSentDict(sentDict)
    tweet_json=[]

    for tweet in tweets_file:
        try:
            #print "try1"
            tweet_json.append(json.loads(tweet))  # all tweets loaded from json to tweet_json
        except:
            pass

    texts = []

    for x in tweet_json:
        try:
           #print "try2"
            texts.append(x['text'])   #only the tweet texts loaded in texts list
        except:
            pass
    
    for tweet in texts:
        tweet_terms = getENTweet(tweet)
        nTerms = len(tweet_terms)
        score, uTerms = tweetAnalysis(tweet_terms, sentDict, tweet)
        genPredSentDict(score, nTerms, uTerms, newSentDict)     #score= full tweet score, nterms = number of all terms in tweet, uterms = unknown terms list, newsentdictionary is a new dictionary
        
    return newSentDict


def getPredSentDict(sentDict, tweets_file): #method1
    predDict = initPredSentDict(sentDict, tweets_file)
    refinePredSentDict(predDict)
    return predDict


if __name__ == '__main__':
    predDict = getPredSentDict(sys.argv[1], sys.argv[2])
    printSentDict(predDict)
