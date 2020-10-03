from textblob import TextBlob
import sys
import os
import re
import tweepy
from tweepy import OAuthHandler
import matplotlib.pyplot as plt



def percentage(part, whole):
    return 100 * float(part)/float(whole)


oauth_consumer_key = "HwlLA16FBvHXiKn5RonmEP3u8"
oauth_consumer_secret = "ARSuGRuvvLI6pRbL4WnvpyGuJFkBJA42PvOsa8dPD47xZ3rFKp"
oauth_token= "1550899406-VONt2jKp2xuBN0veiscfCzybFFejdikNee8YaRv"
oauth_token_secret = "tyAfBYjbH2YfJqprVPd6nxn5kjQqhmdTJRWqiqmHWjCAw"


auth = tweepy.OAuthHandler(oauth_consumer_key, oauth_consumer_secret)
auth.set_access_token(oauth_token,oauth_token_secret) 
api= tweepy.API(auth)



searchTerm = input("Enter Keyword: ")
noOfSearchTerms = int(input("*Enter Many Tweeets Want To Analyze: "))


tweets = tweepy.Cursor(api.search ,q=searchTerm, lang="id", since='2020-09-26', until='2020-10-02').items(noOfSearchTerms)


positive = 0
negative = 0
neutral = 0
polarity = 0



for tweet in tweets:
   
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity


    if(analysis.sentiment.polarity == 0):
        neutral += 1
    elif(analysis.sentiment.polarity < 0.00):
        negative += 1
    elif(analysis.sentiment.polarity > 0.00):
        positive += 1

positive = percentage(positive, noOfSearchTerms)
neutral  = percentage(neutral ,noOfSearchTerms)
negative = percentage(negative, noOfSearchTerms)


positive = format(positive, '.2f')
neutral  = format(neutral ,'.2f')
negative = format(negative, '.2f')


print("How People Reacting On " + searchTerm + " by Analyzing "+str(noOfSearchTerms)+" Tweets")

        
if(polarity == 0):
     print('Neutral')
elif(polarity < 0):
    print('Negative')
elif(polarity > 0):
    print('Positive')


labels = ['Positive['+str(positive)+'%]', 'Neutral['+str(neutral) +'%]','Negative['+str(negative)+ '%]']
sizes  = [positive, neutral, negative]
colors =  ['yellowgreen', 'gold', 'red']
patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, labels, loc="best")
plt.title("How People Reacting On " + searchTerm + " by Analyzing "+str(noOfSearchTerms)+" Tweets")
plt.axis('equal')
plt.tight_layout()
plt.show()
