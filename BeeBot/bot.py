import os
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
    await bot.say("https://pastebin.com/6Wgh7Ua1")
    await bot.say("^code^")

@bot.event
async def on_member_join(member):
    with open("users.json", "r") as f:
        users = json.load(f)
  
    await update_data(users, member)

    with open ("users.json", "w") as f:
        json.dump(users,f)

@bot.event
async def on_message(message):
     with open("users.json", "r") as f:
        users = json.load(f)
     
     await update_data(users, message.author)
     await add_experience(users, message.author, 5)
     await level_up(users, message.author, message.channel)

     
     
     with open ("users.json", "w") as f:
        json.dump(users,f)
    

async def update_data(users, user):
    if not user.id in users:
        users[user.id] = {}
        users[user.id]["experience"]=0
        users[user.id]["level"] = 1

async def add _experience(users, user, exp):
    users[user.did]["experience"] += exp


async def level_up(users, user, channel):
    experience = users [user.id]["experience"]
    level_start = users[user.id]["level"]
    level_end = int(experience ** (1/4))


    if level_start < level_end:
        await bot.send_message(channel, "{} has bee'd up to bee {}").format(user.mention, level_end)
        users[user.id]["level"] = level_end


bot.run("NDk4MjAyMDQ3OTUxMTQyOTIz.DpqYmw.pwDF_e4h4Ty7Hf0skKH2PX-GxPQ")



