import os
import sys
import time
import random
import discord
import youtube_dl

sys.path.insert(0, '\\wsl$\Arch/home/annoyingapple/Code-ish/Aroke\'s\ Maid/commands')

from commands import music
from discord.ext import commands, tasks
from discord.ext.commands import Bot
from dotenv import load_dotenv

load_dotenv()

client = commands.Bot(command_prefix = '~')#, intents = discord.Intents.all())
status = ['Cleaning the house', 'Feeding the pet', 'Cooking some food']

@tasks.loop(seconds=20)
async def change_status():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(random.choice(status)))

@client.event
async def on_ready():
    change_status.start()
    print('Bot started as {0.user}'.format(client))

async def on_message(message):
    author = message.author
    content = message.content
    channel = message.channel
    if message.author == client.user:
        return

@client.command()
async def ping(ctx):
    await ctx.send(f'Ping: {round(client.latency * 1000)}ms')

@client.command(pass_context=True)
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send('Message(s) deleted.')
    time.sleep(1)
    await ctx.channel.purge(limit=1)

@client.command(aliases=['8ball', 'ask'])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]
    await ctx.send(f'{random.choice(responses)}')

client.run(os.getenv('TOKEN'))