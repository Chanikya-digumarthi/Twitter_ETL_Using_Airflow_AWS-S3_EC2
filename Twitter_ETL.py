
# Import modules
import pandas as pd
import numpy as np
import tweepy as ty
import json
from datetime import datetime
import s3fs


#Twitter account keys
api_key = "ekiO4EQmpzMGgwifkeDk1VFtw"
api_secret = "ACljEwqUNoLfWi40HHW35oRj4BgJcrW299iQfK7ADyrtZAnKay"
access_key = "1594811930107158603-dDyGdTHmWGS79v1pR9alOzp1yc2B92"
access_secret = "HayXRQDQQMGKq7Q4Nju2Xt0kosWorqbc7Ys8MonzfA2vq"


def run_etl_airflow():
    # Twitter Authentication
    auth = ty.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_key, access_secret)


    #Create an api object
    api = ty.API(auth)

    tweets = api.user_timeline(screen_name = '@elonmusk',
                               count = 1000,
                               include_rts = False,
                               tweet_mode = 'extended'
                               )


    tweet_list = []
    for tweet in tweets:
        text = tweet._json["full_text"]
        refined_tweet = {"user": tweet.user.screen_name,
                         'text': text,
                         'favorite_count': tweet.favorite_count,
                         'retweet_count': tweet.retweet_count,
                         'created_at':tweet.created_at      
                         }
        tweet_list.append(refined_tweet)

    df = pd.DataFrame(tweet_list)
    df.to_csv("s3://airflow-etl-twitter-s3-chan/elon_musk_tweets.csv")

