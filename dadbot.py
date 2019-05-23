import time
import tweepy
import requests
import json
import re



CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''


INTERVAL = 3600 #tweets every hour
#INTERVAL = 15  # every 15 seconds, for testing
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True:
	for tweet in tweepy.Cursor(api.search,q = "I’m -filter:retweets lang:en",exclude_replies = True, tweet_mode='extended').items():
		print('FULL TWEET '+tweet.full_text)
		try:
			phrase = tweet.full_text.encode()
			phrase = re.split("im | Im | IM | I'm | I'M | i'm", phrase)[1]
			phrase = 'Hi '+ phrase + ", I'm Dad"
			print("Final phrase: "+phrase)
		except:
			break

		try:
			tweetId = tweet.id
			username = tweet.user.screen_name
			api.update_status("@" + username + " " + phrase, in_reply_to_status_id = tweetId)
			print ("Replied with " + phrase)

		except tweepy.TweepError as e:
			print(e.reason)

		except StopIteration:
			break

		time.sleep(INTERVAL)
