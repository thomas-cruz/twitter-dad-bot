# coding: utf-8
import time
import tweepy
import unidecode



CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''


INTERVAL = 3600 #tweets every hour
#INTERVAL = 120  # every 15 seconds, for testing
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
a = ["I’m", "i’m",  "im",  "Im",  "IM",  "I'm",  "I'M",  "i'm"]
test = "I'm so glad I don't fuck my followers. 😂 This shit finna get messy. Lmao."


while True:
	for tweet in tweepy.Cursor(api.search,q = "I'm -filter:retweets lang:en",exclude_replies = True, tweet_mode='extended').items():
		print('FULL TWEET '+tweet.full_text)
		try:
		   print("shit")
		   test = tweet.full_text.replace('\n', ' ').encode('ascii', 'ignore').decode('ascii', 'ignore')
		   phrase = unidecode.unidecode(test)
		   print("shitter " + phrase)
		   if any(s in phrase for s in a):
			#tried re.split before, was hit or miss. going loco with this one
		       test = phrase.replace("im ", '`').replace("Im ", '`').replace("IM ", '`').replace("I'm ", '`').replace("I'M ", '`').replace("i'm ", '`').split('`')		   else:
		       phrase = ''
		   print(test)
		   test = filter(None, test)
		   phrase = test[-1]
		except:
		    print("restart me")
		    sys.exit()

		phrase = 'Hi '+ phrase + ", I'm Dad"
		print("Final phrase: "+phrase)

		if(len(phrase.strip()) != 0):
		    try:
		        tweetId = tweet.id
		        username = tweet.user.screen_name
		        api.update_status("@" + username + " " + phrase, in_reply_to_status_id = tweetId)
		        print ("Replied with " + phrase)
		        time.sleep(INTERVAL)
		    except tweepy.TweepError as e:
		         print(e.reason)
		    except StopIteration:
		         break
