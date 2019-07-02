import tweepy
from textblob import TextBlob

consumer_key ="FdEZe4ivj3BUsWkCCSdl9MnLm"
consumer_secret = "9xIOeJ5jhHfhMq9lSA3fDkGdjRJ9kJxetzGPPvxC62QLtJZdlj"

access_token = "712015203601231872-6BlqL8kNiBfmdpuIgPxVpkBLR4obdSA"
access_token_secret= "htJEqjJYxwOkuVKyxSBcMQp38Vdp79ug9mbOGjq7qIpnn"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('krishna yele')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)