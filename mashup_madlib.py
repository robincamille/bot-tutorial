#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Mad Lib Maker!

# This script will generate mad-libs based off of a William Carlos
# Williams poem, 'The Red Wheelbarrow.' Each poem will then be
# tweeted by your bot account. 

# Housekeeping: do not edit
import json, io, tweepy, time, urllib2
from random import randint
from credentials_lacunybot import *
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


# Housekeeping: opening JSON files
# Find more item lists at https://github.com/dariusk/corpora/tree/master/data
# Click "Raw" button, copy URL
list1file = urllib2.urlopen('https://raw.githubusercontent.com/dariusk/corpora/master/data/objects/objects.json')
list1read = list1file.read()

list2file = urllib2.urlopen('https://raw.githubusercontent.com/dariusk/corpora/master/data/foods/menuItems.json')
list2read = list2file.read()

list3file = urllib2.urlopen('https://raw.githubusercontent.com/dariusk/corpora/master/data/humans/occupations.json')
list3read = list3file.read()

# Create Python-readable lists of items in JSON files
list1 = json.loads(list1read)['objects'] # Change 'objects' to the title of the list
list2 = json.loads(list2read)['menuItems']
list3 = json.loads(list3read)['occupations']


# Repeatable poem-generator
poemlist = []
counter = 0

while counter < 1: # Change 2 to however many poems you want to produce
    
    # Pick random numbers
    list1num = randint(0, len(list1) - 1)
    list2num = randint(0, len(list2) - 1)
    list3num = randint(0, len(list3) - 1)

    # Choose random items from each list using random numbers
    first = list1[list1num] # Syntax: list[number]
    second = list2[list2num].lower()
    third = list3[list3num].lower() + 's'

    # Fill in the blanks of the poem
    poem = 'so much depends\nupon\n\na\n%s\n\nglazed with\n%s\n\nbeside the\n%s\n\n' \
           % (first, second, third)

    print poem
    poemlist.append(poem) #add to long list of poems
    counter = counter + 1


# Line up tweets for bot

for line in poemlist: 
    api.update_status(line)
    #print line
    time.sleep(15) # Sleep for 15 seconds


print '[All done!]'

