import tweepy
import time

consumer_key="stsY7lMpccp39pCQaxfiakphx"
consumer_secret="kFIFF8BcdnJFu4jNv5DDoOXQyKxVRBTVT9rbhjB3s8LxWY7YQN"
key="1354332471702110208-MfH9dQdUOvjXtCZ9jwbKDOSC7hVoVk"
secret="uWaRLYqPCm1qjneTjUUQoogd3O5Hz7Aoob9gacwr7wltL"

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