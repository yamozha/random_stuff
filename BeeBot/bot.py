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
    """yeet"""
    await bot.say(":bee: yeet :bee:")


@bot.listen()
async def on_message(message):
    if "thanos car" in message.content:
        await bot.say(message.channel, ":bee: fuck you :bee: ")


@bot.command()
async def code(message):
    """Code repository"""
    await bot.say("https://github.com/yamozha/random_stuff/tree/master/BeeBot")
    await bot.say(":bee: ^code^ :bee:")


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
        await bot.send_message(channel, ":bee: {} has bee'd up to bee {} :bee:".format(
            user.mention, level_end))
        userExpData[user.id]["level"] = level_end


@bot.command(pass_context=True)
async def levelcheck(context):
    """Checks your level"""
    global userExpData, bot
    await bot.say(":bee: Your level is :bee:")
    await bot.send_message(context.message.channel,
	userExpData[context.message.author.id]["level"])

async def perma_save():
    await asyncio.sleep(30)
    save_user_data()
    await perma_save()


load_user_data()
bot.loop.call_soon(perma_save)
bot.run(TOKEN)
bot.close()
save_user_data()
