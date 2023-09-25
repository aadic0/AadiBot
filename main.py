"""
This is meant to be a personal use discord bot for Aadi's personal discord server.
This bot has access to a wide range of free APIs that work with news, weather, and of course the native Discord API.

Future additions:
The next addition to this bot will include acess to the Reddit API, allowing for access to different top reddit posts from different communities. If this works well, this will also replace the current news API.
Planning to add a blackjack feature. The plan is to have a money system that saves by writing to a text file. The money available to each person is a set amount initially and can be gambled to increase/decreased with equal odds of winning or losing. This will be a fun feature to play with friends.

Known problems:
The news API is often tricked into thinking ads are part of the top news stories. When displaying the top news stories, the ad is also displayed.
"""

# Import discord.py. Allows access to Discord's API. Also set up intents.
import discord
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True

# Import commands from the discord.ext module.
from discord.ext import commands
# Import the os module.
import os
   
# Import load_dotenv function from dotenv module.
from dotenv import load_dotenv

# Import pickle so we can read and write dictionaries to files. Will use dump() and load() methods for gambling feature.
import pickle
  
# Other common modules to be imported.
from datetime import datetime
import requests
import time

# REDDIT API VARIABLES (WIP)
client_id_reddit = "qvpKu3TkrMjTFEoWDdbdbw"  # Should store client_id_reddit as a secret.
REDDIT_SECRET = os.getenv("REDDIT_SECRET")

# auth_reddit = requests.auth.HTTPBasicAuth(client_id_reddit, REDDIT_SECRET)

# with open('pwus.txt', 'r') as f:
#   pw = f.read()

# data_reddit = {
#   'grant_type': 'password',
#   'username': 'momgeyforme', #should store reddit username and password as secret
#   'password': 'chauhan246'
# }

# headers = {'User-Agent': 'MyAPI/0.0.1'}
# res = requests.post('https://www.reddit.com/api/v1/access_token', 
#                    auth=auth_reddit, data=data_reddit, headers=headers)
# REDDIT_TOKEN = res.json()["access_token"]
# headers['Authorization'] = f'bearer {REDDIT_TOKEN}'

# res = requests.get('https://oauth.reddit.com/r/python/hot', headers=headers)
# print(requests.get('https://oauth.reddit.com/api/v1/me'))  

# WEATHER API VARIABLES
api_key = "771039d4d2dbb03fa15e888c1b70e2fb"
city = "Calgary"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric";
response = requests.get(url)
data = response.json()
temp = data["main"]["temp"]
weather = data["weather"][0]["description"]
timestamp = data["dt"]
dt_object = datetime.fromtimestamp(timestamp)

# NEWS API VARIABLES'
country = "Canada"
api_key_news = "18a1e61d97e44f2c93772a03b0362920"
url_news_global = f"https://newsapi.org/v2/top-headlines?apiKey={api_key_news}&pageSize=5&sources=bbc-news,cnn,fox-news,the-new-york-times,the-washington-post"
url_news_local = f"https://newsapi.org/v2/top-headlines?q={country}&apiKey={api_key_news}&pageSize=5"

gresponse_news = requests.get(url_news_global)
gdata_news = gresponse_news.json()
garticle_1 = gdata_news["articles"][0]
garticle_2 = gdata_news["articles"][1]
garticle_3 = gdata_news["articles"][2]
garticle_4 = gdata_news["articles"][3]
garticle_5 = gdata_news["articles"][4]

lresponse_news = requests.get(url_news_local)
ldata_news = lresponse_news.json()
larticle_1 = ldata_news["articles"][0]
larticle_2 = ldata_news["articles"][1]
larticle_3 = ldata_news["articles"][2]
larticle_4 = ldata_news["articles"][3]
larticle_5 = ldata_news["articles"][4]

loopBool = True

startTime = time.time()

# Loads the .env file that resides on the same level as the script.
load_dotenv()

# Grab the Discord API token from the .env file.
DISCORD_TOKEN = os.getenv("TOKEN")

# Creates a new Bot object with a specified prefix.
bot = commands.Bot(command_prefix="$")

# GambleSaves code
open('gambleSaves.txt', 'r+')

#Dhanbot main code
# client.on("ready", async () => {
#   const myGuild = client.guilds.cache.get(guildId)
#   await myGuild.setIcon("./images/image.png")
# })

@bot.command()
async def status(ctx):
  await ctx.channel.send("Working!")

@bot.event
async def on_message(message):
	if message.content == "hi":
		await message.channel.send("Hello")
	await bot.process_commands(message)

@bot.command() # future code for gamble feature
async def Gamble(ctx):
  pass

@bot.command()
async def Globalnews(ctx):
  title_news_1 = garticle_1["title"]
  summary_news_1 = garticle_1["description"]
  
  title_news_2 = garticle_2["title"]
  summary_news_2 = garticle_2["description"]
  
  title_news_3 = garticle_3["title"]
  summary_news_3 = garticle_3["description"]
  
  title_news_4 = garticle_4["title"]
  summary_news_4 = garticle_4["description"]
  
  title_news_5 = garticle_5["title"]
  summary_news_5 = garticle_5["description"]

  await ctx.channel.send(f"Here are some news titles for you:\n\n{title_news_1}\n*{summary_news_1}*\n\n{title_news_2}\n*{summary_news_2}*\n\n{title_news_3}\n*{summary_news_3}*\n\n{title_news_4}\n*{summary_news_4}*\n\n{title_news_5}\n*{summary_news_5}*")

@bot.command()
async def Localnews(ctx):
  title_news_1 = larticle_1["title"]
  summary_news_1 = larticle_1["description"]
  
  title_news_2 = larticle_2["title"]
  summary_news_2 = larticle_2["description"]
  
  title_news_3 = larticle_3["title"]
  summary_news_3 = larticle_3["description"]
  
  title_news_4 = larticle_4["title"]
  summary_news_4 = larticle_4["description"]
  
  title_news_5 = larticle_5["title"]
  summary_news_5 = larticle_5["description"]

  await ctx.channel.send(f"Here are some news titles for you:\n\n{title_news_1}\n*{summary_news_1}*\n\n{title_news_2}\n*{summary_news_2}*\n\n{title_news_3}\n*{summary_news_3}*\n\n{title_news_4}\n*{summary_news_4}*\n\n{title_news_5}\n*{summary_news_5}*")

@bot.command()
async def Weather(ctx):
  await ctx.channel.send(f"Weather conditions in Calgary: {weather}\n Values were measured at {dt_object}")

@bot.command()
async def Temp(ctx):
  await ctx.channel.send(f"Temperature for Calgary in Celsius: {temp}\n Values were measured at {dt_object}")

@bot.command()
async def meow(ctx):
	await ctx.channel.send("meowwwwwwww")

@bot.command()
async def SpamPing(ctx, arg):
  for i in range(0, int(arg)):
    await ctx.channel.send("<@" + str(496879909130600448) + ">")
    time.sleep(0.5)

@bot.command()
async def LabeebBirthday(ctx, arg):
  for i in range(0, int(arg)):
    await ctx.channel.send("HAPPY BIRTHDAY <@" + str(310893877605302272) + ">")
    time.sleep(0.5)

@bot.command()
async def TimeRunning(ctx):
  endTime = time.time()
  timeElapsed = endTime - startTime
  await ctx.channel.send(f"I have been running for {timeElapsed:.2f} seconds")

@bot.command()
async def version(ctx):
  version = 3.6
  await ctx.channel.send(f"Aadi has updated me to version {version}.")

@bot.command()

async def Kick(ctx, member: discord.Member, *, reason=None):
  if ctx.author.id == 433039309365575700 or ctx.author.id == 689620980645363715 or ctx.author.id == 236683717903384576:
    try:
      await member.kick(reason=reason)
      await ctx.send(f'User {member} has kicked.')
    except:
      await ctx.send("Test Failed")
  else:
    await ctx.send("Nice try, no perms")

@bot.command()
async def Test1(ctx:commands.Context):
    await ctx.channel.purge(limit=1)
    guild = ctx.guild
    with open("memberids.txt", "w") as file:
        for member in guild.members:
            file.write(str(member.id)+"\n")
    await ctx.send("Memeber IDs sucessfully collected!",delete_after=10)

@bot.command()
async def Test2(ctx: commands.Context):
    with open("memberids.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            true_id = int(line.strip())
            await ctx.send(f"<{true_id}>")

bot.run(DISCORD_TOKEN)
