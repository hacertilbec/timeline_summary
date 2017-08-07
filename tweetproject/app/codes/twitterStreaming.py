#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy

# The user credentials to access Twitter API 
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

def get_timeline():
	# This handles Twitter authetification and the connection to Twitter Streaming API
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)

	# User's home timeline tweets 
	public_tweets = api.home_timeline(count=100) 
	timeline = [tweet.text.encode("utf-8") for tweet in public_tweets]
	return timeline

if __name__ == '__main__':
	get_timeline()
