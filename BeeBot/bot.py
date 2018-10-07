
import discord
from discord.ext import commands
import asyncio
import json


description = '''beebot'''
bot = commands.Bot(command_prefix='b?', description=description)
os.chdir(r'/Projects/random_stuff/BeeBot')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def nasty():
     await bot.say("yeet")


@bot.listen()
async def on_message(message):
     if "bee" in message.content:
         await bot.send_file(message.channel,"./bee.png")


@bot.listen()
async def on_message(message):
    if "thanos car" in message.content:
	    await bot.say("fuck you")

@bot.command()
async def code():
    await bot.say("https://github.com/yamozha/random_stuff/tree/beebot/BeeBot")
    await bot.say("^code^")

