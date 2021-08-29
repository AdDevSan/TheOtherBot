import asyncio
import discord
import emoji
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

TOS = None
totalMembers = 0

#Member Count VC
mCCID = 881167786674651136

client = commands.Bot(command_prefix='$',intents=discord.Intents.all())
client.remove_command("help")

@client.event
async def on_ready():
    print("bot ready")
    global TOS, totalMembers

    TOS = client.get_guild(758958473424797738)  #The Other Side Server
    mCC = client.get_channel(mCCID) #mCC Member Count Channel Variable
    
    while True:
        totalMembers = len([m for m in TOS.members if not m.bot])
        await mCC.edit(name=f"Member Count: {totalMembers}")

@client.command()
async def hi(ctx):
    await ctx.send("Hello")

client.run('NzU5MDA2OTE4NTYyOTM4ODkx.X23ORw.QLjkR8jXZk9Lb0lVM4XcP65CUtQ')