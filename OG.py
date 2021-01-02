#import keep_alive
import discord
from discord.ext import commands
import os
import requests
import json
import random
from dotenv import load_dotenv
from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
print(os.getenv('TOKEN'))
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

bot = commands.Bot(command_prefix="$")
'''
encouragments
'''
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]
starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person / bot!"
]
'''
#roles
'''

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    

@bot.event
async def on_message(message):
    if any(word in message.content for word in sad_words):
      await message.channel.send(random.choice(starter_encouragements))
    await bot.process_commands(message)
@bot.command(
	# ADDS THIS VALUE TO THE $HELP PING MESSAGE.
	help="Uses come crazy logic to determine if pong is actually the correct value or not.",
	# ADDS THIS VALUE TO THE $HELP MESSAGE.
	brief="Prints pong back to the channel."
)
async def ping(ctx):
	# SENDS A MESSAGE TO THE CHANNEL USING THE CONTEXT OBJECT.
        print("ping sent")
        await ctx.channel.send("pong")
@bot.command(
        name="hello",
        help="Greetings",
        brief="Says hello" 
)
async def hello(ctx):
    print(ctx.author)
    await ctx.channel.send("Hello {}".format(ctx.author))
    role = discord.utils.find(lambda r: r.name == "botter", ctx.message.author.guild.roles)
    print(role)
    if role not in ctx.author.roles: 
        print("not in")
        print(ctx.author.roles)
        roleToAdd = discord.utils.get(ctx.author.guild.roles, name = "botter")
        print(roleToAdd)
        await ctx.author.add_roles(roleToAdd,reason="interaction")

@bot.command(
        name="inspire",
        help="I'm here to inspire you",
        brief="a bot to inspire you"
        )
async def inspire(ctx):
    quote = get_quote()
    await ctx.channel.send(quote)

#keep_alive.keep_alive()
bot.run(os.getenv('TOKEN'))

