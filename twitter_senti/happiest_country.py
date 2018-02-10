# Required imports or library dependencies
import re, sys, json
from tweet_sentiment import *
from stateDict import getStatesDict
from matlibbbb import *

#happiest countries except US
# Is the tweet from a certain country?
def isCountry(tweet_json, country = 'United States'):
    try: return tweet_json['place']['country'] == country
    except: return False
    

# Get abbreviated state's form from encrypted place info
# Fill me.
def getStateFromPlace(placeInfo):

    return stateABV


# Gets the state (cond. USA) info of the tweet.
def getUSAStateABV(tweet_json):
    try:
        placeInfo = tweet_json['place']['full_name']        
        stateABV = getStateFromPlace(placeInfo)
        return stateABV
    except: ''


# Is the state in the United States?
# Returns true flase.
# Fill me
"""def isStateInUSA(tweet_json, stateList):
    try: 

    except: return False"""


# Is the tweet geo coded?
def isGeoEnabled(tweet_json):
    return tweet_json['user']['geo_enabled']


# Fill the rest.
# Details explained in class
def mostHappyCountries(sentDict, tweets_file): #method 1
    stateSenti = {} #statesenti will have key:statecode , value: score
    statesList = getStatesDict() #imported method
    tweets_file = open(tweets_file)
    sentDict = genSentDict(sentDict)
    tweet_json = []

        
    for tweet in tweets_file:
        try:
            #print "try1"
            tweet_json.append(json.loads(tweet))  # all tweets loaded from json to tweet_json
        except:
            pass

    """texts=[]
    for x in tweet_json:
        try:
           #print "try2"
            texts.append(x['place']['country_code'])   #only the tweet texts loaded in texts list
        except:
            pass

    for y in texts:
        print y
        """

    for x in tweet_json:
        try:
            if x['place']['country'] in stateSenti.keys():
                stateSenti[x['place']['country']]+=getSentScoreOfTweet(x['text'],sentDict)#score is the score of the tweet
            else:
                stateSenti[x['place']['country']]=0
                stateSenti[x['place']['count']]+=getSentScoreOfTweet(x['text'],sentDict)
        except:
            pass

    stateSenti.pop("United States")

    for x in stateSenti.keys():
        value = stateSenti[x]
        print("%s %.4f" % (x, value))

    plotFrequencyBar(stateSenti)


    #sortDict = sorted(stateSenti, key=stateSenti.get)
    #print statesList[sortDict[-1]]

        
if __name__ == '__main__':
    mostHappyCountries(sys.argv[1], sys.argv[2])
