#Twitter bot tutorial
This tutorial and its materials were put together by Robin Davis (@robincamille) and Mark Eaton (@MarkEEaton) for a December 15, 2015 workshop for librarians sponsored by the [LACUNY Emerging Technologies Committee](http://commons.gc.cuny.edu/groups/lacuny-emerging-technologies-committee/). You can use these materials any which way; the following instructions are for our workshop. 

See also: Davis, Robin, and Mark Eaton. [Make a Twitter Bot in Python: Iterative Code Examples](http://jitp.commons.gc.cuny.edu/make-a-twitter-bot-in-python-iterative-code-examples/). *Journal of Interactive Technology and Pedagogy*,  April 2016. (Verbose write-up featuring code in this repository.)

**Required libraries:** tweepy, setuptools, json, urllib2 or urllib3

##Download the files
See the "Download ZIP" button toward the upper right? Click it and save the folder to your desktop. 

##Create a Twitter account for your bot

1. Go to http://twitter.com and sign up for a new account of your choosing.
 - Be sure to include your mobile number (required for using the API) 
 - Email address must be unique to Twitter users; try adding random periods in your Gmail address, if you have one

2. Go to http://apps.twitter.com and create a new app
 - This info isn't public so it can be messy 
 - Go to Keys and Access Tokens
 - Create new access token

3. Copy Consumer Key/Secret and Access Key/Secret to **credentials.py**

##Basic bot: mybot.py
This script is a basic Twitter bot. It will tweet three things from a **list** inside the script.

1. Right-click on mybot.py and select Edit with IDLE

2. Take a look at the script; Robin and Mark will talk about what it's doing

3. Select Run > Run Module from the window's menu bar

*Change it up!*
- In **tweetlist**, add new things for your bot to tweet. 
- Increase/decrease time between tweets in **time.sleep(15)** (15 is the number of seconds). 

##Intermediate bot: mybot2.py
This script sends out five tweets from the first five lines of an external .txt file.

1. Right-click on mybot.py and select Edit with IDLE

2. Right-click on twain.txt and open it in Notepad

3. Take a look at both files; Robin and Mark will talk about what the script is doing

4. Select Run > Run Module from the window's menu bar for mybot2.py

*Change it up!*
- Go to http://gutenberg.org and choose a different text for your bot to tweet. 
 - Download the file as "plain text" into the tutorial folder and open it in Notepad
 - Remove junk at the beginning of the file
 - Replace double linebreaks with single linebreaks with a find/replace
 - In mybot2.py, replace twain.txt with the name of the new text file 
- Make the bot send more or fewer tweets, or change which lines, by editing the numbers in **for line in tweettext[0:5]**. 
 - [0:5] means from the first thing up to (but not including) the fifth thing
 
##Advanced bot: mashup_madlib.py
This script treats *The Red Wheelbarrow* as a mad-lib, filling in three blanks from two data sources: JSON files from @dariusk's [collection of corpora](https://github.com/dariusk/corpora). 

##Advanced bot: respondingbot.py
This script from Mark tweets a random line from a .txt file whenever @jasonchowbot tweets.

##Advanced bot: mashup_markov
This script uses a Markov chain to create new sentences from another text, and tweets them.

