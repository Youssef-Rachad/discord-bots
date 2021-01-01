import keep_alive
import discord
import os
import requests
import json
import random

client = discord.Client()

'''
encouragments
'''
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]
starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person / bot!"
]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
@client.event
async def on_message(message):
    print(message.author)
    #print(message.author.color)
    role = await message.guild.create_role(name="botter", color = discord.Color(0x0000FF))
    await message.author.add_roles(role)
    if message.author == client.user:
        return
    if message.content.startswith('$Hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('$inspire'):
      quote = get_quote()
      await message.channel.send(quote)
    if any(word in message.content for word in sad_words):
      await message.channel.send(random.choice(starter_encouragements))


keep_alive.keep_alive()

client.run(os.getenv('TOKEN'))

