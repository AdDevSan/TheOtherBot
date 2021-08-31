import asyncio
import discord
import emoji
import json
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure
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

@client.event
async def on_member_join(member):

    #edits member count channel
    mBChannel = client.get_channel(allChannelID["member-count"])
    totalMembers = len([m for m in TOS.members if not m.bot])
    await mBChannel.edit(name = f"Members: {totalMembers}")

    #pings user in reaction roles channel
    jjID = member.id
    rrc = TOS.get_channel(allChannelID["reaction-roles"])
    ping = await rrc.send(f"<@!{jjID}>")
    await ping.delete()

@client.event
async def on_member_remove(member):
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

    


courseRoles = [
    ['Accounting'],['Actuarial'],['Architecture'],['AppMath'], ['AppChemistry'], ['BioInformatics'],['Biology'],
['BusinessAdmin'], ['ComSci'],['Communications'], ['Civil Engineering'],['China Studies'], ['DigitalMedia'], ['Finance'],
['EconFinance'],['Environmental Science'],['English'],['ElectricalEngineering'], ['ItlBusiness'],['IndustryDesign'],
['IntelRobotics'],['InformationSys'],['ManufaEngineering'],['Marketing'],['MechaEngineering'],['TeleCom'],
['TV Production'],['UrbanDesign']]


@client.command()
async def course(ctx,*,roleIN):

    #algo to find closest string to input
    roleOUT = process.extract(roleIN, courseRoles, limit=5)

    #saves highest ratio string to roleVAR
    roleVAR = roleOUT[0][0][0]



    # INTITIAL EMBED------------------------------------------------------------------------------
    embed=discord.Embed(title="Course Roles", description= f"results for \"{roleIN}\" :", color=0x1271c4)
    embed.set_footer(text=f"requested by - @{ctx.message.author.name}   |   react to a role accordingly")
    count = 0
    valid = False
    #list to refer to discord number emote
    numdict = ((0,':zero:'),(1,':one:'), (2, ':two:'),(3,':three:'),(4,':four:'),(5,':five:'),

               (6,':six:'),(7,':seven:'),(8,':eight:'),(9,':nine'))

    #EMOLIST-----------------------
    emolist = []

    # ADDS FIELD FOR EVERY ROLE TO BE PUT IN MENU
    for roleOut in roleOUT: #roleOut example: (['BioInformatics'], 90)


        #if ratio is greater than 60 and ratio diff between first ratio and other ratio less than 25
        if roleOut[1] > 60 and (roleOUT[0][1] - roleOut[1]) <= 25:
            count += 1
            embed.add_field(name = "\u200b", value = f'{numdict[count][1]} - {roleOut[0][0]}' ,inline = True)
            prevRatio = roleOut[1]
          #appends number emoji & role name to emolist
            emolist.append([numdict[count][1], roleOut[0][0]])
            valid = True

    #adds cancel option if valid
    if valid:
        embed.add_field(name = "\u200b", value = emoji.emojize(f':no_entry_sign: - Cancel Request', use_aliases = True) ,inline = False)

   # if ratio too low: valid = false ; process ends after embed sent
    if valid == False:
        embed.add_field(name = "\u200b", value = f'your search was off-limits, please try again...' ,inline = False)

    #THIS LINE SENDS THE EMBED------------------------------------------------------------------
    justSent = await ctx.send(embed=embed)

    # if valid == True
    if valid:

        #THIS LINE PROVIDES THE REACTION ROLES BASED ON EMOLIST----------------------------------------
        for emo in emolist:
            await justSent.add_reaction(emoji.emojize(emo[0], use_aliases = True))

        #ADDS CANCEL BUTTON REACTION
        await justSent.add_reaction(emoji.emojize(":no_entry_sign:", use_aliases=True))

        #FROM PYTHON DISCORD SERVER
        def check(r,m):
            return m == ctx.author and r.message.channel == ctx.channel

        #try for timeout
        try:
            reaction, user = await client.wait_for('reaction_add', check=check, timeout=20) #timeout 20s

            if reaction.emoji is not None:

                #loops through each i[0] in emolist -> [[':one:', 'BioInformatics'], [':two:','Biology']]
                mRole = ""

                #Flag to test if reaction is cancel or other emoji
                roleFound = False

                #Loop to find corresponding emoji
                for i in emolist:
                    #if :one:/:two:/:three: == reacted emoji
                    if emoji.emojize(i[0], use_aliases=True) == reaction.emoji:
                        #Flag = True
                        roleFound = True
                        #gets corresp. role name from emolist, place it in mRole variable
                        mRole = i[1]

                         #gets role from server based on name from emolist and corresp. emoji react
                        matchingRole = discord.utils.get(ctx.guild.roles, name=mRole)

                    #if the emoji matches role (not cancel)
                if roleFound:
                    
                    #REMOVES AUTHOR EXISTING CLASS ROLES FUNCTION-----------------------------------

                     # takes all roles from author to be put in m_role
                    m_role = []
                   
                    # for every role in author roles
                    for mem_role in ctx.author.roles:
                        m_role.append(mem_role)

                    # compares courseRoles to author's roles and removes any existing course roles
                    for _ in courseRoles:
                        for i in m_role:
                            if i.name == _[0]:
                                await ctx.author.remove_roles(i)

                    #gives author role
                    await ctx.author.add_roles(matchingRole)
            

                    # SUCCESS EMBED------------------------------------------------------------------------------------
                    # removes embed desc
                    editEmbed = discord.Embed(title="Course Roles", description="\u200b", color=0x1271c4)
                    # edits field
                    editEmbed.add_field(name=f" role \"{mRole}\" successfully added!", value='\u200b', inline=True)
                    editEmbed.set_footer(text=f"requested by - @{ctx.message.author.name}")
                    await justSent.edit(embed=editEmbed)
                    await justSent.clear_reactions()

                #if cancel----------------------------------------------------------------
                else:
                    cancelEmbed = discord.Embed(title="Course Roles", description="\u200b", color=0x1271c4)
                    # edits field
                    cancelEmbed.add_field(name=emoji.emojize("  :no_entry_sign:   Request Cancelled!",use_aliases = True), value='\u200b', inline=True)
                    cancelEmbed.set_footer(text=f"requested by - @{ctx.message.author.name}")
                    await justSent.edit(embed=cancelEmbed)
                    await justSent.clear_reactions()

        #TimeOut Error Response
        except asyncio.TimeoutError:

            #TIMEOUT ERROR EMBED---------------------------------------------------------------------------------
            editEmbed2 = discord.Embed(title="Course Roles", description="\u200b", color=0x1271c4)
            editEmbed2.add_field(name=f"TimeoutError!", value="be faster next time you slowpoke!", inline=False)
            editEmbed2.set_footer(text=f"requested by - @{ctx.message.author.name}")
            await justSent.edit(embed=editEmbed2)
            await justSent.clear_reactions()


@client.command()
@has_permissions(administrator = True)
async def addcrr(ctx):
    reactionRolesChannel = TOS.get_channel(allChannelID['reaction-roles'])
    mathEmbed=discord.Embed(title="Math Modules", description="basically ur modules that generally requires more thinking & logic...", color=0xe91e63)
    mathEmbed.add_field(name="Year 1", value="\u200b", inline=False)
    mathEmbed.add_field(name="MTH015", value="\u200b", inline=True)
    mathEmbed.add_field(name="MTH025/27", value="\u200b", inline=True)
    mathEmbed.add_field(name="MTH023", value="\u200b", inline=True)
    mathEmbed.add_field(name="Year 2", value="\u200b", inline=False)
    mathEmbed.add_field(name="MTH", value="\u200b", inline=True)
    mathEmbed.add_field(name="MTH", value="\u200b", inline=True)
    mathEmbed.add_field(name="\u200b", value="\u200b", inline=True)
    await ctx.send(embed=mathEmbed)
    
    


@client.command()
@has_permissions(administrator=True)
async def addClass(ctx,*,className):
    print(className)





#--------------------------------------------------------
client.run('NzU5MDA2OTE4NTYyOTM4ODkx.X23ORw.QLjkR8jXZk9Lb0lVM4XcP65CUtQ')

"NzU5MDA2OTE4NTYyOTM4ODkx.X23ORw.QLjkR8jXZk9Lb0lVM4XcP65CUtQ" #real bot
"NzU5NzE0NzgyMDU5NTYwOTgw.X3Bhhg.NyOghAJIG1M70qTpNH7OExpn7xY" #test 