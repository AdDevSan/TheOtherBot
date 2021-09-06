import asyncio
import discord
import emoji
import json
import random
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


variablesr = open('variables.json','r')

#dictionaries
allChannelID = json.load(open('channel_id.json','r'))
variablesDict = json.load(variablesr)
modulesDict = json.load(open('modules.json', 'r'))
#------------------------------------------------------
#Global Variables
TOS = None

year_roles = {"1️⃣": 759014288043671602,
                "2️⃣": 759014527211143178,
                "3️⃣": 759014621473538070,
                "4️⃣": 759014693057855518,
                "💡": 880688917895065630,
                "🖇️": 880689672307740672}

rY1 = None
rY2 = None
rY3 = None
rY4 = None
rM = None
rO = None
cY1 =  0
cY2 =  0                                
cY3 =  0
cY4 =  0
cM = 0
cO = 0






client = commands.Bot(command_prefix='$',intents=discord.Intents.all())
client.remove_command("help")

#list to refer to discord number emote
numdict = ((0,':zero:'),(1,':one:'), (2, ':two:'),(3,':three:'),(4,':four:'),(5,':five:'),

            (6,':six:'),(7,':seven:'),(8,':eight:'),(9,':nine:'))
emojiList = [
        '😀', '🥰', '😴', '🤓', '🤮', '🤬', '😨', '🤑', '😫', '😎',
    '🐒','🐕','🐎','🐪','🐁','🐘','🦘','🦈','🐓','🐝','👀','🦴','👩🏿','🤝','🧑','🏾','👱🏽','🎞','🎨','⚽',
    '🍕','🍗','🍜','☕','🍴','🍉','🍓','🌴','🌵','🛺','🚲','🛴','🚉','🚀','✈','🛰','🚦','🏳','‍🌈','🌎','🧭',
    '🔥','❄','🌟','🌞','🌛','🌝','🌧','🧺','🧷','🪒','⛲','🗼','🕌','👁','‍🗨','💬','™','💯','🔕','💥','❤',
]

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


    #Role Giver in Year Roles Embed------------------------------------------------------
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
        selectRole = TOS.get_role(year_roles[emojiChoice])
        await getMember.add_roles(selectRole)

        #pings user and send confirm message
        await TOS.get_channel(allChannelID["bot-commands"]).send(f"<@!{payload.user_id}> role `{selectRole}` awarded!")


            
  




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


<<<<<<< HEAD
@client.command()
@has_permissions(administrator = True)
async def addcrr(ctx):
    modulesDict = json.load(open('modules.json', 'r'))
    
    await ctx.send("Select Category:")

    count = 1
    menu1 = {}
    catList = []

    #appends unique categories into catList
    for module in modulesDict:
        cat = modulesDict[module]['category']

        #if category in dictionary not yet in catlist, catlist gets appended category
        try:
            catList.index(cat)
        except ValueError:
            catList.append(cat)
    
    #sends category choices to discord
    for i in catList:
        await ctx.send(f"{count}. {i}")
        menu1[f"{count}"] = i
        count += 1

    def check(m):
        return m.author == ctx.author and len(m.content) == 1

    try:
        userM1 = await client.wait_for('message', check=check, timeout=20)
        userC1 = userM1.content
        try:
            #checks if userC1 (user choice) is part of menu1 (dictionary)

            userChoice = menu1[userC1]
            print(menu1[userC1])
            list1 = []
            list2 = []
            list3 = []
            list4 = []
            catModules = [list1,list2,list3,list4]
            #TODO: get all modules from modulesDict with said category
            count = 1

            for module in modulesDict:
                
                mod = modulesDict[module]

                if mod["category"] == userChoice:

                    #sorting algorithm
                    
                    catModules[int(mod["year"])-1].append([module, mod["year"], mod["emoji"]])

                    
            for list in catModules:
                list.sort()
                

            #TODO: build embed seperate by years
            embed=discord.Embed(title="Class Roles", description=userChoice, color=0xE91E63)

            yearVar = 1
            emojiOptionsList = []
            for i in catModules:
                if len(i) >0:
                    embed.add_field(name=f"Year {yearVar}", value="\u200b", inline=False)
                    yearVar += 1
                    for j in i:
                        embed.add_field(name=f"\u2800\u2800{j[0]}    {emojiList[j[2]]}\u2800\u2800", value="\u200b", inline=True)
                        emojiOptionsList.append(emojiList[j[2]])
            
            embed.set_footer(text=f"TheOtherSide 另一边 | 2020 | Can't find your module? Contact staff so we can add!")
            classReactionMessage = await client.get_channel(allChannelID["bot-test"]).send(embed=embed) 
            #TODO: save embed ID and save it in json
            
            #TODO: assign reaction emojis

            for emoji in emojiOptionsList:
                await classReactionMessage.add_reaction(emoji)


        except KeyError:
            await ctx.send("Choice is out of bounds!")
    except asyncio.TimeoutError:
        await ctx.send("Terminated!")


    
    '''reactionRolesChannel = TOS.get_channel(allChannelID['bot-test'])
    sampleList = []
    #TODO: Function to send embeds and add reactions
    for key in modulesDict:

        category = modulesDict[key]
        count = 0
        embed=discord.Embed(title=f"{key}", description="basically ur modules that generally requires more thinking & logic...", color=0xe91e63)
        
        for year in category: #year are keys, categories = modulesDict[key]

            #if modules in years greater than 0
            moduleList = category[year]
            if len(moduleList) > 0:
                embed.add_field(name=f"Year {year}", value="\u200b", inline=False)         
                print(moduleList)

            for i in moduleList: #category are the lists inside the nested dictionary

                embed.add_field(name=f"{i}", value="\u200b", inline=True)
                count +=1
                print(F"count: {count}")
        crr = await reactionRolesChannel.send(embed=embed)
        sample = random.sample(emojiList, count)

        for i in sample:
            await crr.add_reaction(i)
        sampleList.append(sample)
    '''

    
    

=======
>>>>>>> master

@client.command()
@has_permissions(administrator=True)
async def addclass(ctx,*,className):
    modulesDict = json.load(open('modules.json', 'r'))
    specDict = {"name":className,
                "category":None,
                "year":None,
                "emoji":None
                }
    #TODO: add conditionals
    await ctx.send("Select Category:")

    count = 1
    menu1 = {}
    catList = []

    #appends unique categories into catList
    for module in modulesDict:
        cat = modulesDict[module]['category']

        #if category in dictionary not yet in catlist, catlist gets appended category
        try:
            catList.index(cat)
        except ValueError:
            catList.append(cat)
    
    #sends category choices to discord
    for i in catList:
        await ctx.send(f"{count}. {i}")
        menu1[f"{count}"] = f"{i}"
        count += 1

    await ctx.send(f"{count}. add new category")


    #TODO: append class to json file
    def check(m):
        return m.author == ctx.author and len(m.content) == 1
    
    def checkYear(m):
        condition1 = (m.author == ctx.author and len(m.content) == 1)
        condition2 = (int(m.content) > 0 and int(m.content) <= 4) 
        return condition1 and condition2
    #waits for author message reply
    try:
        userM1 = await client.wait_for('message', check=check, timeout=20)
        userC1 = userM1.content
        proceed = True #first declare

        
        try:
            #checks if userC1 (user choice) is part of menu1 (dictionary), sets it as specDict ['category']
            specDict['category'] = menu1[userC1]

            proceed = True

        #This checks if option chosen is add new category or isn't valid
        except KeyError:


            
            #if userC1 is last choice of menu1
            if int(userC1) == len(catList)+1:
                await ctx.send("Enter New Category:")

                try: #waits for user reply on new category name
                    userNewCat = await client.wait_for('message', check=None, timeout=20)
                    userNewCatC = userNewCat.content

                    #add confirmation feature here
                    await ctx.send(f"type \"{userNewCatC}\" again to confirm new category:")
                    try:
                        catConfirm = await client.wait_for('message', check=None, timeout=20)
                        
                        #if confirmation successful
                        if catConfirm.content == userNewCatC:
                            
                            specDict['category'] = userNewCatC
                            await ctx.send(f"New Category {userNewCatC} confirmed!")
             
                            proceed = True

                        #if confirmation fails
                        else:
                            await ctx.send("Confirm did not match, please try again from the beginning!")
                            proceed = False

                    #if timeout
                    except asyncio.TimeoutError:
                        await ctx.send("Terminated!")
                        proceed = False
                except asyncio.TimeoutError:
                    await ctx.send("Terminated!")
                    proceed = False
            
            #if userC1 is out of bounds
            else:
                await ctx.send("Invalid Option !")
                proceed = False

        #continue with year here
        if proceed:
            await ctx.send("What Year?")

            try: #waits for user response on year value
                yearIN = await client.wait_for('message', check=checkYear, timeout=20)
                specDict['year'] = int(yearIN.content)
     

               
                emoList = []

                #appends all emoji value from dictionary where items match the new class category
                for module in modulesDict:
                    innerDict = modulesDict[module]
                  
                    if innerDict['category'] == specDict['category']:
                           
                        emoList.append(innerDict['emoji'])
                        
                        
                
                #makes rangeList - a list that contains the available choices where 1 value
                #will then be randomly drawn
                rangeList = []
                for i in range(72):
                    rangeList.append(i)
                for i in emoList:
                    rangeList.remove(i)
                randomVar = random.choice(rangeList)

                
                #enters the randomly drawn emoji value in specDict
                specDict['emoji'] = randomVar

               
                
                #make new role
                newRole = await ctx.guild.create_role(name=specDict['name'], colour=discord.Colour(0xE91E63) )
                specDict['role_id'] = newRole.id
                await ctx.send(f"{specDict['name']} role created! (id:{newRole.id})")
                #make channel
                modCategory = discord.utils.get(TOS.categories, name = "Modules")
                newChannel = await modCategory.create_text_channel(specDict['name'])
                specDict['channel'] = newChannel.id

                #set channel permissions to new class role and all classes
                
                allClassesRole = TOS.get_role(variablesDict['all_classes_role'])
                await newChannel.set_permissions(TOS.default_role, view_channel=False)
                await newChannel.set_permissions(newRole, view_channel = True)
                await newChannel.set_permissions(allClassesRole, view_channel = True)
                
                await ctx.send(f"{specDict['name']} text channel created! (id:{newChannel.id})" )
                
                #await client.create_role(TOS, name="NewClass", colour=discord.Colour(0xffffff))

                #update specDict to modules.json 
                modulesDict[specDict['name']] = {"category": specDict["category"],
                                                "year":specDict["year"],
                                                "emoji":specDict["emoji"],
                                                "role":specDict["role_id"],
                                                "channel":specDict['channel']
                                            }
                json.dump(modulesDict, open('modules.json','w'))
                await ctx.send("modules.json updated!")
                #TODO: update reaction roles embed



            except asyncio.TimeoutError:
                    await ctx.send("Terminated!")

    except asyncio.TimeoutError:
        await ctx.send("Terminated!")


@client.command()
async def demo(ctx):

    await ctx.channel.set_permissions(TOS.default_role, view_channel=False)
    await ctx.send("done")



#--------------------------------------------------------
client.run('NzU5MDA2OTE4NTYyOTM4ODkx.X23ORw.QLjkR8jXZk9Lb0lVM4XcP65CUtQ')

"NzU5MDA2OTE4NTYyOTM4ODkx.X23ORw.QLjkR8jXZk9Lb0lVM4XcP65CUtQ" #real bot
"NzU5NzE0NzgyMDU5NTYwOTgw.X3Bhhg.NyOghAJIG1M70qTpNH7OExpn7xY" #test 