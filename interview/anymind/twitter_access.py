import tweepy
import json

consumer_key = 'd7gdxpbOIpimj20mIWLQYUhnS'
consumer_secret = 'WUyiK12UOLUVGn9jv3ODXFssrdpKLv3vYi42IeoA3F399gKtIF'
access_token = '570534552-dT1cV6AGW5B4p8XNhEJm62wbnuygnStQ6Rf9oo5V'
access_token_secret = 'ojIu80CK9nCPFa6YePPxJVLs1DLS0gF8fj6050zsJbAo6'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)


def process_or_store(tweet):
    print(json.dumps(tweet))


def get_tweet_by_hash_tag(str):
    params = {
        'q': str,
        'lang': "en",
        'count': 100,
        # 'since': "2018-05-13",
    }
    for tweet in tweepy.Cursor(api.search, **params).items():
        print(tweet.created_at, tweet.text)
        # process_or_store(tweet._json)


def get_tweet_by_user(str):
    params = {
        'screen_name': str,
        # 'lang': "en",
        'count': 200,
        # 'since': "2018-05-13",
    }
    for tweet in tweepy.Cursor(api.user_timeline, **params).items():
        print(tweet.created_at, tweet._json)
        # process_or_store(tweet._json)


get_tweet_by_hash_tag("#python")
get_tweet_by_hash_tag("@addyosmani")
get_tweet_by_user("addyosmani")
get_tweet_by_user("AddyOsmani")


