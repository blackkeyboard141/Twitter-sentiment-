# Required imports or library dependencies
import re, sys, json, enchant
d= enchant.Dict("en_US")



# Is the tweet in English?
# Use try and except clause
# If try works for english language tweet return true, else false
# Read Twitter Developer Documentation carefully
def isLang(tweet_json):
    try: # Fill me check if each word is english
        #print "try5"
        d.check(tweet_json) #this checks if each word is english
        return True
    except: return False


# Create a sentiment dictionary
def genSentDict(sent_file):
    sent_file = open(sent_file)
    scores = {}
    
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)        # Convert the score to an integer.        
    
    return scores


# Get a English tweet 
# Check for English Tweets 
# input: tweet as json
# output: tweet terms as list

# Make sure to use unicode encode
# Use re.findall to get the tweet terms/words as list.
# Fill the rest.
# Details explained in class.
def getENTweet(tweet_json):
    # Fill me - Break tweets here into words , check each word if english and put it into list. tweet_json here is a string
    tweet_json=tweet_json.lower()
    tweet_json = re.sub(r"[^A-Za-z]", " ", tweet_json.strip()) #this takes out all the numbers and special characters, only keeps the english alphabets
    words = tweet_json.split() #this splits and lists the string to individual words

    tweet_terms = []
    for x in words:
        try:
            #print "try4"
            isLang(x) #this checks each words in the tweet string if english
            tweet_terms.append(x) #this populates the list tweet_terms
        except:
            pass
    #print tweet_terms
    return tweet_terms #this is the list of english terms in the tweet


    

# Get score from the tweet
# input: tweet as json, sentiment dictionary (hashmap and/or map, python dictionary)
# output: tweet score
# Fill the rest, details explained in class.
def getSentScoreOfTweet(tweet_json, sentDict):
    #tweet_json has 1 tweet in each case
    tweet_score = 0
    tweet_terms = getENTweet(tweet_json)    #tweet_terms has the list of english words in a tweet, tweet_json is a string

    for term in tweet_terms:
        try:
            #print "try6"
            tweet_score = tweet_score+sentDict[term] #this calculates value of each term from the dictionary if I am not mistaken
        except:
            pass

    return tweet_score

# Score the tweets in the tweets file
def getTweetScores(sentDict, tweets_file):
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

    x=0
    for y in texts:
        try:
            #print "try3"
            score = getSentScoreOfTweet(y, sentDict)#sending each tweet texts, getting values and printing them
            #x=x+1
            print score

        except: pass
   # print x




if __name__ == '__main__':
    getTweetScores(sys.argv[1], sys.argv[2])
