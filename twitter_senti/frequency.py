import re, sys, json
from tweet_sentiment import *
from matlibbbb import *

# Fill the rest
# Details explained in class.
# Input: The downloaded tweets file
# Output: The freq dictionary {key: tweet terms, value: frequency as probability}
def frequency(tweets_file):
    freq = {}
    tweets_file = open(tweets_file)
    tweet_json=[]
    tweet_terms = []

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


    for y in texts:
        try:
            tweet_terms.append(getENTweet(y))
        except:
            pass


        #for term in tweet_terms:
            #term = term.lower()

    #print tweet_terms

    for z in tweet_terms:
        for i in range(0, len(z)):
            if(z[i] in freq):
                freq[z[i]]+=1
            else:
                freq[z[i]]=0
                freq[z[i]]+=1

    sortedWords = sorted(freq,
                        key=freq.get,
                        reverse=True)[:20]

    plotFrequencyBar(freq)
	
        
    for x in sortedWords:
        value = freq[x]
        print("%s \t %.4f" % (x, value))

def printFrequency(freqDict):
    for key in freqDict.keys():
        print("%s %.4f" % ( key, freqDict[key] ) )
        #print ""

if __name__ == '__main__':
    frequency(sys.argv[1])
    
