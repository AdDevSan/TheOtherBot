import asyncio
import discord
import emoji
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

newVar = 0 #declare newVar

client = commands.Bot(command_prefix='$',intents=discord.Intents.all())
client.remove_command("help")

@client.event
async def on_ready():
    print("bot is ready...")
    global newVar
    newVar = 1 
    print(f"print 1: {newVar}") #print 1

@client.command()
async def hi(ctx):
    print(f"print 2: {newVar}") #print 2


client.run('NzU5MDA2OTE4NTYyOTM4ODkx.X23ORw.QLjkR8jXZk9Lb0lVM4XcP65CUtQ')