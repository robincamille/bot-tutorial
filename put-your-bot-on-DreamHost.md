# Put your Twitter bot on DreamHost 

*Written June 2018*

You don't have to run your bot from your desktop! You can, but it will shut down every time your computer does. Host your bot instead! 

I use [DreamHost](https://www.dreamhost.com/) and like them a lot. If you happen to have a DreamHost hosting account, these instructions will work for you. I have no idea if any of the below instructions work for other hosting services. ¯\\\_(ツ)\_/¯


Caveats:
- **Intermediate and advanced users only!** You should already know how the command line works and what commands like `cd` and `chmod` mean. 
- Fair warning, these instructions might be wrong or out of date. You should only follow along if you know what you're doing. 
- These instructions are for DreamHost users only. 

## Make the virtual environment & install Tweepy
This is an essential step: it installs Python and makes it possible to use Python libraries, like Tweepy. By default, the below directions installs an isolated Python 2.7 for you. If you need Python 3, see Notes below.

This may be the hardest part. You might run into errors. Google them and good luck. 

1. [Use SSH to get to your DreamHost account directory](https://help.dreamhost.com/hc/en-us/articles/216041267-SSH-overview)
1. Get to your home directory (one level above the directories that contain your hosted websites)
2. Issue this command: `virtualenv mybots`
    - This creates a new folder, `mybots`.
1. `cd mybots` 
1. `python -V` (just to check your Python version). 
	- If it's a version you don't like, try to finagle a new version of Python or just give up and go with the flow.
3. Activate your virtual environment with `source bin/activate`
    - Your SSH prefix will now look like `(mybots)[servername]$`
4. `pip install tweepy` 
1. Pip install any other libraries you require
5. `deactivate`

### Notes about this step
- You shouldn't have to fool around with virtualenv after this step, except for updating or adding libraries. 
- I'm still using Python 2.7 but am getting an error message from one of my libraries every time a bot tweets, soooo I'll get around to changing up to Python 3 soonish
- [Python2 virtualenv directions](https://help.dreamhost.com/hc/en-us/articles/215489338-Installing-and-using-virtualenv-with-Python-2) from DreamHost
- [Python3 virtualenv directions](https://help.dreamhost.com/hc/en-us/articles/115000695551-Installing-and-using-Python-s-virtualenv-using-Python-3) from DreamHost

## Put your files in mybots/
1. Using an FTP client (I like [Transmit](https://www.panic.com/transmit/) for Mac), navigate to your `mybots/` folder.
1. Upload your bot's `.py` script(s) in there, along with any data files (like `.txt` files the bots use). 
	- These files will reside on the same level as `bin/` and the other directories that were automatically added when you installed the virtual environment.

## Make a shell script
1. Make a new plaintext file that says this: 
> `#!/bin/bash`
>
> `cd /home/yourusername/mybots`
>
> `source bin/activate`
>
> `python tweetscript.py`

2. The directory after `cd` will differ for you: be sure to change `yourusername`, `mybots`, and `tweetscript.py` accordingly. 
1. Save this file as `make_bot_tweet.sh` or similar. Add it to `mybots/` alongside your script.
1. ⚠️ **Important!!** In your FTP client or through SSH, be sure that your `make_bot_tweet.sh` has User Execute permissions. (a.k.a., chmod 744.)

## Set up cron job
A cron job is a task that is done periodically on a server or other operating system. You can it to run every hour, day, etc. 
1. Log into the [DreamHost control panel](https://panel.dreamhost.com/). 
1. On the left, under Goodies, find **Cron jobs**.
1. Add a new Cron Job.
	- **User**: the username you put your `twitterbots` directory under
	- **Title**: something descriptive that makes sense to you, like `poembot`
	- **Email output to**: add in your email address at first. Any error messages will get sent to you. You can remove it once you're sure your bot works.
	- **Command to run**: `/home/yourusername/mybots/make_bot_tweet.sh`
	- **When to run**: Up to you! I like using Custom and setting it to run at Selected Minutes (like every :25), and every hour, day, month, and day of week.
		- For testing purposes, choose a Selected Minutes that's like 10 minutes from now so you can see soon enough when it runs, but not so soon that any server settings won't take effect. 
	
## Does your bot work? 
- At the moment the bot should run, take a look at your bot's Twitter page. Does a new tweet appear? 
- If not, did you get an error message by email? 
	- You might get an error message even if the tweet is sent. For example, I get an `InsecurePlatformWarning` all the time because I'm still using Python 2.7. 
- At some point, your bot will stop working, likely because modules need an update or the Twitter API has changed. Make sure your email is in the cron job to get notified of error messages.

### Common error messages
- `sh: /home/yourusernamehere/mybots/make_bot_tweet.sh: Permission denied`
	- You need to fix the permissions of your `.sh` script. 
		- In an FTP client, make sure User has Execute permission. 
		- Via SSH, run `chmod 744 make_bot_tweet.sh`.
- `tweepy.error.TweepError: [{u'message': u'Bad Authentication data.', u'code': 215}]`
	- Check your credentials.py file again. Note that the access token has a hyphen in it, so you might’ve copied/pasted wrong from apps.twitter.com. 
	- You can test your bot from your desktop to check your credentials.
- `tweepy.error.TweepError: [{u'message': u'Status is a duplicate.', u'code': 187}]`
	- You can’t send the exact same tweet within a given time period. Just add another character to it or change it entirely.
- `ImportError: No module named _io` (or similar module errors)
	- If this is an unusual library that you had to install yourself, activate the virtual environment again and pip install that library.
	- If it's a module that should be included by defalt, like `\_io`, rebuild the virtual environment. It's a pain (and you'll have to move your bot files to the new directory you make in the process) but necessary, as this is likely a problem with updates from the host’s side that aren’t reflected in your virtual environment.
- Another Python warning not listed here? Fix your script! Run it on your desktop before uploading it to DreamHost and waiting for the cron job to run. 

## Tips for running multiple bots
- Each bot should have its own credentials, Python script, and `.sh` script. These 3 files should be consistently named for your own organization - e.g., give them all the same prefix.
- Cron jobs are bot-specific.
- Ensure that the bot's Twitter handle is in its Python script or credentials file so you can keep things straight.



RCD • June 11, 2018
