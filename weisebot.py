#Simple bot for Twitter handle @WeiseBot created by @WeiseGamer, aka Thomas Hughes'''
#Source can be found (sans the covert.py which contains API tokens/keys) at https://github.com/weiseguy

import os
import tweepy
from covert import *
from time import gmtime, strftime

#~~~~~~~~Bot Auth Setup~~~~~~~~~#

botHandle = "WeiseBot"
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
twitterAPI = tweepy.API(auth)

#~~~~~~~End Bot Setup~~~~~~#

