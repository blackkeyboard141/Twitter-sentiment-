# Required imports or library dependencies
import re, sys, json
from tweet_sentiment import *
from matlibbbb import *

# Fill me.
# Details explained in class.
def gettopTenHashTags(tweets_file, n = 10):
    tags = {}
    tweets_file = open(tweets_file)
    tweet_json = []
    hashtags=[]
        
    for tweet in tweets_file:
        try:
            tweet_json.append(json.loads(tweet))
        except:
            pass

    for y in tweet_json:
        try:
            hashtags.append(y['entities']['hashtags']) #hashtags will have all the hashtags now
        except:
            pass

    for z in hashtags:
        for i in range(0,len(z)):
            try:
               # print z[i]['text']
                if z[i]['text'] in tags:
                    tags[z[i]['text']]+=1
                else:
                    tags[z[i]['text']]=0
                    tags[z[i]['text']]+=1
            except:
                pass


    sortedTags = sorted(tags,
                        key=tags.get,
                        reverse=True)[:10]
    
    for x in sortedTags:
        value = tags[x]
        print("%s \t %.4f" % (x, value))

    plotFrequencyBar(tags)


        
if __name__ == '__main__':    
    gettopTenHashTags(sys.argv[1])

    
    
    
