#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Twitter Bot Starter Kit: Bot 1

# This bot tweets three times, waiting 15 seconds between tweets.

# If you haven't changed credentials.py yet with your own Twitter
# account settings, this script will tweet at twitter.com/lacunybot

# Housekeeping: do not edit
import tweepy, time
from credentials import *
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


# What the bot will tweet

tweetlist = ['Test tweet one!', 'Test tweet two!', 'Test tweet three!']

for line in tweetlist: 
    api.update_status(line)
    print line
    print '...'
    time.sleep(15) # Sleep for 15 seconds

print "All done!"


