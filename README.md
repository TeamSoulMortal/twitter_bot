# Twitter Bot
This is a Twitter bot with Auto retweet , Auto like , Auto Follow feature 
running with the help of tweepy module
Use with Termux for best results! 

REQUIREMENTS :
1. A working internet connection 
2. Termux app downloaded from F-droid.org as Google play store version is outdated
3. Tweepy module 
4. Python3 
5. Pip
6. Nano for editing the file
7. wget to download files from this git id

To install required files use my one click command
Copy this command and paste it into termux and hit enter 
And wait patiently let the script do its job

```
sh -c "$(curl -fsSL https://raw.githubusercontent.com/TeamSoulMortal/twitter_bot/main/autoinstall.sh)"
```

After installation
To run the bot all you have to do is enter API keys in credentials.py
With the help of nano tool, use Ctrl+X to save your modifications :) 
Then run this command below
```
python3 twitterbot.py
```

And voila your bot should start Retweeting, Following, Liking the posts under
the tag you entered inside config.py

And to stop the bot use Ctrl+C

Have fun :) 
