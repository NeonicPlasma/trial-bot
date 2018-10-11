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

trialsServer = 'hi'

startTimes = {}
peopleDoingChallenge = []

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
    user = ctx.message.user
    if guild:
        await ctx.send('**You can only use this in DMs.**')
    else:
        await ctx.send('Challenge is starting! Starting in 10 seconds, get ready!')
        await asyncio.sleep(5)
        await ctx.send('**Challenge has started!**')

@bot.command()
async def deleteMessage(ctx):
    await bot.wait_until_ready()
    await ctx.send(ctx.message.guild.id)
    global trialsServer
    msg = await ctx.send("Message deleted in 5 seconds. This bot comes from " + trialsServer + ".")
    await asyncio.sleep(5)
    await msg.delete()
        

        
bot.run("")
