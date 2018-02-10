import re, sys, json
from tweet_sentiment import *
from stateDict import getStatesDict

statesList = getStatesDict()

x = 'WA'

#print statesList

if x in statesList:
    print "yes"



#print statesList