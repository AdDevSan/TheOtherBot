import asyncio
import discord
import emoji
import json
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


variablesr = open('variables.json','r')

#dictionaries
allChannelID = json.load(open('channel_id.json','r'))
variablesDict = json.load(variablesr)

#------------------------------------------------------
#Global Variables
TOS = None

year_roles = {"1️⃣": 759014288043671602,
                "2️⃣": 759014527211143178,
                "3️⃣": 759014621473538070,
                "4️⃣": 759014693057855518,
                "💡": 880688917895065630,
                "🖇️": 880689672307740672}

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

@client.event
async def on_member_join(ctx):

    #edits member count channel
    mBChannel = client.get_channel(allChannelID["member-count"])
    totalMembers = len([m for m in TOS.members if not m.bot])
    await mBChannel.edit(name = f"Members: {totalMembers}")

@client.event
async def on_member_remove(ctx):
    #edits member count channel
    mBChannel = client.get_channel(allChannelID["member-count"])
    totalMembers = len([m for m in TOS.members if not m.bot])
    await mBChannel.edit(name = f"Members: {totalMembers}")

#---------------------------------------------------------------------------------------------
#Year Reaction Message
Year_Message = 759024782405926952
#Year Roles
@client.event
async def on_raw_reaction_add(payload):
    yearReactMessage = variablesDict["year_react_message"]


    #Role Giver in Year Roles Embed
    if payload.message_id== yearReactMessage:

        m = await client.get_channel(payload.channel_id).fetch_message(yearReactMessage)
        emojiChoice = payload.emoji.name
        getMember = TOS.get_member(payload.user_id)

        memRoleList = getMember.roles
        memRoleIDList = []

        #removes the reaction in embed message
        await m.remove_reaction(emojiChoice, payload.member)

        for roles in memRoleList:
            memRoleIDList.append(roles.id)

        #compares roles in dictionary year_roles with member roles, appends existing year roles to list
        existingYearRoles = []
        for key in year_roles:
            for roleID in memRoleIDList:
                if year_roles[key] == roleID:
                    existingYearRoles.append(memRoleList[memRoleIDList.index(roleID)])
        
        #removes all member roles that is in list existingYearRoles
        print(existingYearRoles)
        if len(existingYearRoles) > 0:
            for role in existingYearRoles:
                await getMember.remove_roles(role)

        #gives member the selected role
        selectRoleID = year_roles[emojiChoice]
        await getMember.add_roles(TOS.get_role(selectRoleID))



            
        




@client.event
async def on_member_update(before,after):

    reactionRolesChannel = client.get_channel(allChannelID['reaction-roles'])
    yearReactionMessage = await reactionRolesChannel.fetch_message(variablesDict["year_react_message"])
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

    # edit the embed of the message
    await yearReactionMessage.edit(embed=embed)
#---------------------------------------------------------------------------------------------



# make sure reaction roles channel ID correct in channel_id.json
@client.command()
@has_permissions(manage_roles=True, ban_members=True)
async def addyrr(ctx):

    await ctx.send("make sure reaction roles channel ID is correct in channel_id.json")
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


    yearReactionMessage = await client.get_channel(allChannelID["reaction-roles"]).send(embed=embed)
    variablesDict['year_react_message'] = yearReactionMessage.id
    json.dump(variablesDict, open('variables.json','w'))

    m = yearReactionMessage
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