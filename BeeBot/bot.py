from config import *
import os
import discord
from discord.ext import commands
import asyncio
import json

description = '''beebot'''
bot = commands.Bot(command_prefix="b?", description=description)
os.chdir(os.path.dirname(os.path.abspath(__file__)))

userExpData = {}


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(
        game=discord.Game(name="b?help"), status=discord.Status("dnd"))


@bot.command()
async def nasty():
    await bot.say("yeet")


@bot.listen()
async def on_message(message):
    if "bee" in message.content:
        await bot.send_file(message.channel, "./bee.png")
    if "thanos car" in message.content:
        await bot.say(message.channel, "fuck you")


@bot.command()
async def code(message):
    await bot.say("https://github.com/yamozha/random_stuff/tree/master/BeeBot")
    await bot.say("^code^")


@bot.event
async def on_member_join(member):
    update_data(member)


@bot.event
async def on_message(message):
    update_data(message.author)
    add_experience(message.author, 5)
    await level_up(message.author, message.channel)
    await bot.process_commands(message)

def load_user_data():
    global userExpData
    with open("users.json", "r") as f:
        userExpData = json.load(f)


def save_user_data():
    global userExpData
    with open("users.json", "w") as f:
        json.dump(userExpData, f)


def update_data(user):
    global userExpData
    if not user.id in userExpData:
        userExpData[user.id] = {
            'experience': 0,
            'level': 1,
        }


def add_experience(user, exp):
    global userExpData
    userExpData[user.id]["experience"] += exp


async def level_up(user, channel):
    global bot, userExpData
    experience = userExpData[user.id]["experience"]
    level_start = userExpData[user.id]["level"]
    level_end = int(experience**(1 / 4))

    if level_start < level_end:
        await bot.send_message(channel, "{} has bee'd up to bee {}".format(
            user.mention, level_end))
        userExpData[user.id]["level"] = level_end


@bot.command(pass_context=True)
async def levelcheck(context):
    global userExpData, bot
    await bot.send_message(context.message.channel,
        userExpData[context.message.author.id]["level"])



load_user_data()
bot.run(TOKEN)
bot.close()
save_user_data()
