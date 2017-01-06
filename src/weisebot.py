#Simple bot for Twitter handle @WeiseBot created by @WeiseGamer, aka Thomas Hughes
#Source can be found (sans the covert.py which contains API tokens/keys) at https://github.com/weisecreations

import tweepy
from covert import *
from time import sleep

#~~~~~~~~Bot Auth Setup~~~~~~~~~#

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
auth.secure = True;
tAPI = tweepy.API(auth)
myBot = tAPI.get_user(screen_name = "@weisebot")

#~~~~~~~End Bot Auth Setup~~~~~~#

#~~~~~~~Search Terms~~~~~~~#

hashTags = ["#IndieDev", "#GameDev", "#PixelArt", "#WeiseBot"]
tweetLanguage = "en"
count403 = 0

#~~~~~~~End Search Terms~~~~~~~#

#~~~~~~~#HashTag RT, Fav, Follow~~~~~~#
i = 0
while i < len(hashTags):
    print("Running bot: @" + myBot.screen_name)
    i += 1

    #Iterates through my hashTag list, RT, Fav, and Follow, 50 each hashTag.
    for tweet in tweepy.Cursor(tAPI.search, q = hashTags[i - 1], lang = tweetLanguage).items(50):
            try:
                #Ensure Tweet isn't from bot
                if (tweet.user.screen_name == myBot.screen_name):
                    print("Found tweet by: @" + tweet.user.screen_name + ", that's me! Skipping!!")
                    continue
                # Log find tweet by @user
                print("Found tweet by: @" + tweet.user.screen_name)

                #Found Tweet bot hasn't RT'd or Fav'd
                if (tweet.retweeted == False or tweet.favorited == False):
                    tweet.retweet()
                    tweet.favorite()
                    print("Retweeted and favorited the tweet")

                #Found User bot hasn't followed
                if (tweet.user.following == False):
                    tweet.user.follow()
                    print("Followed the user")
                count403 = 0 #Successful run, reset count403

            #Error handling
            except tweepy.TweepError as e:
                    print(e.reason)
                    if ("403" in e.reason): #60 mins sleep time if error is limit reached due to multiple 403s
                        if (count403 > 15):
                            print("There are too many 403 errors. Total 403s: " + str(count403) + ", pausing for 60 minutes.")
                            i = 0
                            sleep(3600)
                        else:
                            count403 += 1
                            print("Another 403 error. Total: " + str(count403))
                    else:
                        sleep(10) #Tweeting too fast, error 429, any other errors
                    continue

            except StopIteration:
                i = 0
                break

#~~~~~~~End #HashTag RT, Fav, Follow~~~~~~#
