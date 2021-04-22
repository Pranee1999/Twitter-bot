import tweepy
import time

# Put in the consumer_key
# Put in the consumer_secret
# Put in the key
# Put in the secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

hashtag="100daysofcode"
tweetNumber=10
tweets= tweepy.Cursor(api.search,hashtag).items(tweetNumber)

def search():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweet done!")
            time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)

search()
