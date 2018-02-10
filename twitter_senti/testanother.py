import re, sys, json
tweets = []
texts = []

for line in open('output.json'):
    try:
        tweets.append(json.loads(line))
    except:
        pass

for x in tweets:
    try:
        texts.append(x['text'])
    except:
        pass


print len(texts)
print type(texts)

for y in texts:
    try:
        print y
        print "\n"
    except:
        pass


""""def getTweetScores(tweets_file):
    tweets_file = open(tweets_file)
    #sentDict = genSentDict(sentDict)

   for tweet in tweets_file:
        tweet_json = json.loads(tweet)
        #print tweet_json
    print type(tweet_json)

    print tweet_json[1]

if __name__ == '__main__':
    getTweetScores(sys.argv[1])"""

#----------------------

#Just an example how the dictionary may look like
"""myDict = {'age': ['12'], 'address': ['34 Main Street, 212 First Avenue'],
      'firstName': ['Alan', 'Mary-Ann'], 'lastName': ['Stone', 'Lee']}

def search(values, searchFor):
    for k in values:
        for v in values[k]:
            if searchFor in v:
                return values
    return None

#Checking if string 'Mary' exists in dictionary value
print search(myDict, 'Mary') #prints firstName
print type(myDict)
print search(myDict, 'firstname')

print myDict.get('age')"""

