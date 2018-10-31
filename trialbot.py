import discord
from discord.ext import commands

import random
import asyncio
import os

command_prefix='t.'
bot = commands.Bot(command_prefix)

@bot.event
async def on_ready():
    game = discord.Game("hosting a challenge")
    await bot.change_presence(status=discord.Status.online, activity=game)
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

trialsServer = bot.get_guild(483854858974265344)

novaData = {
 "Starting Time": 0,
 "Finishing Time": 0,
 "Time": 0,
 "Score": 0,
 "Question Number": 0,
 "OWs": 0,
 "EmojiSet1": 0,
 "EmojiSet2": 0,
 "EmojiSet3": 0,
 "Current Stage": 0,
 "StartingChallenge": False,
 "StartedChallenge": False
}

stg1Questions = [
    ["By the end of The Trials stage, who was leading in points?", "tr_", "Supernova727", "So", "A"],
    ["By the end of The Trials stage, who had been UFE the most times?", "turtley", "Achoo", "Lightbat28", "B"],
    ["Who got 1st in Challenge 1?", "Bagels (TheThaiGoat / Henry Kinderman)", "Supernova727", "attacker00", "A"],
    ["Who got 1st in challenge 4?", "attacker00", "So", "tr_", "MrIASA", "B"],
    ["What is the theme color for The Trials (used in artwork a lot)?", "Green", "Yellow", "Red", "Orange", "B"],
    ["What is TrialBot’s tag? (answer it like “t.answer 5352” if you think 5352 was the tag)", "3426"],
    ["How many contestants finished the challenge in Round 1?", "9"]
]
    
async def stage1(user, questionNum):
    global stg1Questions
    global novaData
    questionArray = questionNum - 1
    questionTable = stg1Questions[questionArray]
    question = questionTable[0]
    novaData["Question Number"] = question
    if questionNum <= 3:
        string = "**" + question + "\nA:** " + questionTable[1] + "\n**B:** " + questionTable[2] + "\n**C:** " + questionTable[3]
        await user.send(string)
    elif questionNum <= 5:
        string = "**" + question + "\nA:** " + questionTable[1] + "\n**B:** " + questionTable[2] + "\n**C:** " + questionTable[3] + "\n**D:** " + questionTable[4]
        await user.send(string)
    else:
        string = "**" + question + "**"
        await user.send(string)

@bot.command()
async def startchallenge(ctx):
    guild = ctx.message.guild
    if guild:
        await ctx.send('**You can only use this in DMs.**')
    else:
        await ctx.send('**Are you sure you have at least 10 minutes to complete this challenge?** If you do and would like to do the challenge now, use the command `t.begin`. If you need to stop, use `t.stop`. Once you use the begin command, you cannot stop the challenge. This is timed.')
        
@bot.command()
async def begin(ctx):
    guild = ctx.message.guild
    user = ctx.message.author
    if guild:
        await ctx.send('**You can only use this in DMs.**')
    else:
        await ctx.send('Challenge is starting! Starting in 10 seconds, get ready!')
        await asyncio.sleep(10)
        await ctx.send('**Challenge has started!**')
        await stage1(user, 1)

@bot.command()
async def deleteMessage(ctx):
    await bot.wait_until_ready()
    await ctx.send(ctx.message.guild.id)
    global trialsServer
    msg = await ctx.send("Message deleted in 5 seconds. This bot comes from " + trialsServer.name + ".")
    await asyncio.sleep(5)
    await msg.delete()
        

bot.run(os.getenv('TOKEN'))
