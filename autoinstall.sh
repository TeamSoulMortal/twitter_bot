#!/bin/sh

echo 'Welcome to Automatic Twitter Bot Installer' 
echo 'Script will start installing required packages for you"
echo 'Please be patient while it installs for you'
echo 'Lemme setup termux now and update latest packages' 

pkg update -y && pkg upgrade -y
echo 'Package has been successfully upgraded' 
echo 'Now script will download and install necessary packages' 
echo 'Please be patient while it downloads' 

pkg install python3 nano wget -y
echo 'Success' 
echo 'Now lets get the latest pip version'
python3 -m pip install --upgrade pip
echo 'Script will now download and install Tweepy' 
pip install tweepy
echo 'Tweepy installed successfully' 
echo 'Getting the required files for you' 
wget "https://raw.githubusercontent.com/TeamSoulMortal/twitter_bot/main/config.py"
wget "https://raw.githubusercontent.com/TeamSoulMortal/twitter_bot/main/credentials.py"
wget "https://raw.githubusercontent.com/TeamSoulMortal/twitter_bot/main/twitterbot.py"
echo 'Everything has been installed successfully'
echo 'Enjoy using the bot'
echo 'First add your API keys you got in credentials.py file' 
echo 'Then set required hashtag to be retweeted in config.py file' 
echo 'And finally to use this bot simply type python3 twitterbot.py and hit enter'
