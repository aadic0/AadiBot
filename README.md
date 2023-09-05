# AadiBot
Personal use Discord Bot with access to multiple APIs
This is meant to be a personal use discord bot for Aadi's personal discord server.
This bot has access to a wide range of free APIs that work with news, weather, and of course the native Discord API.

Future additions:
The next addition to this bot will include access to the Reddit API, allowing for access to different top Reddit posts from different communities. If this works well, this will also replace the current news API.
Planning to add a blackjack feature. The plan is to have a money system that saves by writing to a text file. The money available to each person is a set amount initially and can be gambled to increase/decrease fake money with equal odds of winning or losing. This will be a fun feature to play with friends.

Known problems:
The news API is often tricked into thinking ads are part of the top news stories. When displaying the top news stories, the ad is also displayed.
guild.members only returns the bot's information. This means $Test1 returns Aadi Bot's discord ID.
