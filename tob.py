import asyncio
import discord
import emoji
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from fuzzywuzzy import fuzz
from fuzzywuzzy import process



'''client = commands.Bot(command_prefix='$',intents=discord.Intents.all())
client.remove_command("help")'''


#------------------------------------------------------
#Global Variables
TOS = None



year_roles = [["Year 1",759014288043671602],
              ["Year 2",759014527211143178],
              ["Year 3",759014621473538070],
              ["Year 4",759014693057855518],
              ["Masters/PhD",880688917895065630],
              ["Others",880689672307740672]
              ]
rY1 = ""
rY2 = ""
rY3 = ""
rY4 = ""
rM = ""
rO = ""

cY1 =  0
cY2 =  0                                
cY3 =  0
cY4 =  0
cM = 0
cO = 0


print(rY1)

#Reaction Roles Channel
ReactionRoleChannelID = 758998142414225409
RRCnew = 880451939106693171


client = commands.Bot(command_prefix='$',intents=discord.Intents.all())
client.remove_command("help")

#------------------------------------------------------
#Tells if bot is ready
@client.event
async def on_ready():
    print("bot is ready...")

    global TOS, rY1, rY2, rY3, rY4, rM, rO, cY1, cY2, cY3, cY4, cM, cO
    TOS = client.get_guild(758958473424797738)
    rY1 = TOS.get_role(759014288043671602)
    rY2 = TOS.get_role(759014527211143178)
    rY3 = TOS.get_role(759014621473538070)
    rY4 = TOS.get_role(759014693057855518)
    rM = TOS.get_role(880688917895065630)
    rO = TOS.get_role(880689672307740672)

    cY1 = len(rY1.members)
    cY2 = len(rY2.members)                                
    cY3 = len(rY3.members)
    cY4 = len(rY4.members)
    cM = len(rM.members)
    cO = len(rO.members)
    print(rY1)
    print(f"{cY1}  {cY2}  {cY3}  {cY4}  {cM}  {cO}")



#---------------------------------------------------------------------------------------------
#Year Reaction Message
Year_Message = 759024782405926952
#Year Roles
@client.event
async def on_raw_reaction_add(payload):
    if payload.message_id==Year_Message:
        m = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
        if payload.emoji.name == '1️⃣':
            role_id = year_roles[0][1]
            await m.remove_reaction('2️⃣', payload.member)
            await m.remove_reaction('3️⃣', payload.member)
            await m.remove_reaction('4️⃣', payload.member)
        elif payload.emoji.name=='2️⃣':
            role_id=year_roles[1][1]
            await m.remove_reaction('1️⃣', payload.member)
            await m.remove_reaction('3️⃣', payload.member)
            await m.remove_reaction('4️⃣', payload.member)
        elif payload.emoji.name=='3️⃣':
            role_id=year_roles[2][1]
            await m.remove_reaction('2️⃣', payload.member)
            await m.remove_reaction('1️⃣', payload.member)
            await m.remove_reaction('4️⃣', payload.member)
        elif payload.emoji.name=='4️⃣':
            role_id=year_roles[3][1]
            await m.remove_reaction('2️⃣', payload.member)
            await m.remove_reaction('3️⃣', payload.member)
            await m.remove_reaction('1️⃣', payload.member)
        r=client.get_guild(payload.guild_id).get_role(role_id)
        await payload.member.add_roles(r)

@client.event
async def on_raw_reaction_remove(payload):
    if payload.message_id==Year_Message:

        if payload.emoji.name == '1️⃣':
            role_id = year_roles[0][1]

        elif payload.emoji.name=='2️⃣':
            role_id=year_roles[1][1]

        elif payload.emoji.name=='3️⃣':
            role_id=year_roles[2][1]

        elif payload.emoji.name=='4️⃣':
            role_id=year_roles[3][1]

        r=client.get_guild(payload.guild_id).get_role(role_id)
        await client.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(r)
#---------------------------------------------------------------------------------------------




@client.command()
async def blieonwefj(ctx):

    m = await client.get_channel(ReactionRoleChannelID).send("Year of Study Roles (react to 1 only)")
    await m.add_reaction('1️⃣')
    await m.add_reaction('2️⃣')
    await m.add_reaction('3️⃣')
    await m.add_reaction('4️⃣')

@client.command()
@has_permissions(manage_roles=True, ban_members=True)
async def addyrr(ctx):

    rY1 = TOS.get_role(759014288043671602)
    rY2 = TOS.get_role(759014527211143178)
    rY3 = TOS.get_role(759014621473538070)
    rY4 = TOS.get_role(759014693057855518)
    rM = TOS.get_role(880688917895065630)
    rO = TOS.get_role(880689672307740672)

    cY1 = len(rY1.members)
    cY2 = len(rY2.members)                                
    cY3 = len(rY3.members)
    cY4 = len(rY4.members)
    cM = len(rM.members)
    cO = len(rO.members)
    total = cY1 + cY2 + cY3 + cY4 + cM + cO
    embed=discord.Embed(title="Year Roles", description="select a role according to your year of study to gain access to channels ! ", color=0x3900a5)
    embed.add_field(name="Year 1️⃣", value=f"count: {cY1}", inline=True)
    embed.add_field(name="Year 2️⃣", value=f"count: {cY2}", inline=True)
    embed.add_field(name="Year 3️⃣", value=f"count: {cY3}", inline=True)
    embed.add_field(name="Year 4️⃣", value=f"count: {cY4}", inline=True)
    embed.add_field(name="Masters/PhD 💡", value=f"count: {cM}", inline=True)
    embed.add_field(name="Other 🖇️", value=f"count: {cO}", inline=True)
    embed.set_footer(text=f"TheOtherSide 另一边 | 2020 | total: {total}")


    m = await client.get_channel(RRCnew).send(embed=embed)
    await m.add_reaction('1️⃣')
    await m.add_reaction('2️⃣')
    await m.add_reaction('3️⃣')
    await m.add_reaction('4️⃣')
    await m.add_reaction('💡')
    await m.add_reaction('🖇️')



#--------------------------------------------------------
client.run('NzU5MDA2OTE4NTYyOTM4ODkx.X23ORw.QLjkR8jXZk9Lb0lVM4XcP65CUtQ')

"NzU5MDA2OTE4NTYyOTM4ODkx.X23ORw.QLjkR8jXZk9Lb0lVM4XcP65CUtQ" #real bot
"NzU5NzE0NzgyMDU5NTYwOTgw.X3Bhhg.NyOghAJIG1M70qTpNH7OExpn7xY" #test 