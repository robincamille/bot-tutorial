#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Mad Lib Maker!

# This script will generate mad-libbed poems based off of a William Carlos
# Williams poem, 'The Red Wheelbarrow.' Each poem will then be
# tweeted by your bot account. 


import json, io, tweepy, time
from random import randint
from credentials import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


# Open JSON files (lists of things)
# Find more item lists at https://github.com/dariusk/corpora/tree/master/data
    # Click "Raw" button, save file into mashup_madlib folder
infile = open('mashup_madlib/objects.json','r')
objectlist = infile.read()
infile.close()

infile = open('mashup_madlib/menuitemsNYPL.json','r')
foodslist = infile.read()
infile.close()


# Create Python-readable lists of items in JSON files
objs = json.loads(objectlist)['objects']
foods = json.loads(foodslist)['menuItems']


# Repeatable poem-generator
poemlist = []
counter = 0
while counter < 1: # Change 1 to however many poems you want to produce
    
    # Generate random numbers
    objnum = randint(0, len(objs))
    foodnum = randint(0, len(foods))

    # Choose random items from each list
    first = objs[objnum]
    second = foods[foodnum].lower()

    # Fill in the blanks of the poem
    poem = 'so much depends\nupon\n\na\n%s\n\nglazed with\n%s\n\n' % (first, second)

    print poem
    poemlist.append(poem)
    counter = counter + 1


# What the bot will tweet

for line in poemlist: 
    api.update_status(line)
    #print line
    time.sleep(30) # Sleep for 30 seconds


print '[All done!]'

