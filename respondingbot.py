#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Twitter Bot Starter Kit: Responding Bot

# This bot listens to the account @ocertat, and when that account
# tweets, it responds with a line of Twain

# Download a Project Gutenberg "Plain Text UTF-8" file,
# open it in Notepad, remove junk at beginning,
# and replace all double-linebreaks with single linebreaks.


# Housekeeping: do not edit
import tweepy
import time
from credentials import *
from random import randint
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# initially, the script will assume that the last tweet was a null value
lasttweet = None

# What the bot will tweet
filename = open('twain.txt', 'r')
tweettext = filename.readlines()
filename.close()


# a function that picks a random line
def linenum():
    return randint(0, len(tweettext))


# this is the function that does most of the work of the bot
def runTime():

    # uses the global lasttweet variable, rather than the local one
    global lasttweet

    # gets the most recent tweet by @ocertat and prints its id
    mostrecenttweet = api.user_timeline('ocertat')[0]
    print(mostrecenttweet.id)

    # compares the two tweets, and tweets a line of Twain
    # if there is a new tweet from @ocertat
    if mostrecenttweet != lasttweet:
        line = tweettext[linenum()]
        api.update_status(status=line)
        print(line)

    # updates lasttweet to the most recent tweet
    lasttweet = mostrecenttweet

# runs the main function every 5 seconds
while True:
    runTime()
    print("sleeping")
    time.sleep(5)  # Sleep for 5 seconds


# To quit early: CTRL+C and wait a few seconds
