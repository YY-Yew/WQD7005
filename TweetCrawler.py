# -*- coding: utf-8 -*-
import tweepy
import datetime

####Input your credentials here
consumer_key = 'ylpMm2EmxVLREtkap4v59tAzB'
consumer_secret = '9E5ILuIHVoufpuZ2AmF4oKPNUKDckuBHcNS8VFe2OjbQLwAHQa'
access_token = '1107789382293975040-w8JxP2eWQPRQzJGu61y3dQkm9pHi5f'
access_token_secret = 'R2HS4VVpOEfnuSDzG1BoiFSp1IuGQT2pG3fhKAw0y9r5d'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

#####United Airlines
# Open/Create a file
now = datetime.datetime.now()
filename = "Tweet_UA_%s-%s-%s.txt" % (now.day, now.month, now.year)

with open(filename, 'w') as file_object:
    file_object.write("Created_at\tTweet\n")

#Append data
for tweet in tweepy.Cursor(api.search,q="#unitedAIRLINES",count=500,
                           lang="en",since="2018-01-01").items():
    print (tweet.created_at, tweet.text)
    with open(filename, 'a') as file_object:
        file_object.write('%s\t%s\n' % (tweet.created_at, tweet.text.encode('utf-8')))


