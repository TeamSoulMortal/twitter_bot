import tweepy
import time
from time import sleep
from credentials import *
from config import QUERY, LIKE, FOLLOW, RETWEET, SLEEP_TIME

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True)

print("Twitter bot that likes, follows, and retweets based on config.py file")
print("Search criteria -", QUERY)
print("Like user's tweets :", LIKE)
print("Follow user's accounts :", FOLLOW)
print("Re-Tweet user's tweets :", RETWEET)

for tweet in api.search_tweets(q=QUERY):
    try:
        print('\nTweet by: @' + tweet.user.screen_name)

        # check that bot has not already favorited the tweet
        # Favorite the tweet
        if LIKE:
            if not tweet.favorited:
                tweet.favorite()
                print('Liked the tweet')
            
        # Check that bot is not already following the user
        # Follow the user who tweeted
        if FOLLOW:
            if not tweet.user.following:
                tweet.user.follow()
                print('Followed the user')
                
        # Check that bot has not already retweeted the tweet
        # Retweet the tweet
        if RETWEET:
            if not tweet.retweeted:
                tweet.retweet()
                print('Retweeted the tweet')

        sleep(SLEEP_TIME)

    except tweepy.errors.TweepyException as e:
        print(e)

    except StopIteration:
        break

