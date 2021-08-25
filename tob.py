import discord
from discord.ext import commands
from fuzzywuzzy import fuzz
from fuzzywuzzy import process



client = commands.Bot(command_prefix='$',intents=discord.Intents.all())
client.remove_command("help")
#------------------------------------------------------
#Tells if bot is ready
@client.event
async def on_ready():
    print("bot is ready...")
#------------------------------------------------------
year_roles = [["Year 1",759014288043671602],
              ["Year 2",759014527211143178],
              ["Year 3",759014621473538070],
              ["Year 4",759014693057855518]
              ]

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


#Reaction Roles Channel
ReactionRoleChannelID = 758998142414225409

@client.command()
async def blieonwefj(ctx):

    m = await client.get_channel(ReactionRoleChannelID).send("Year of Study Roles (react to 1 only)")
    await m.add_reaction('1️⃣')
    await m.add_reaction('2️⃣')
    await m.add_reaction('3️⃣')
    await m.add_reaction('4️⃣')

courseRoles = [
    ['Accounting'],

    ['Actuarial'],

    ['Architecture'],

    ['AppMath'],

    ['AppChemistry'],

    ['BioInformatics'],

    ['Biology'],

    ['BusinessAdmin'],

    ['ComSci'],

    ['Communications'],

    ['Civil Engineering'],

    ['China Studies'],

    ['DigitalMedia'],

    ['Finance'],

    ['EconFinance'],

    ['Environmental Science'],

    ['English'],

    ['ElectricEngineering'],

    ['ItlBusiness'],

    ['IndustryDesign'],

    ['IntelRobotics'],

    ['InformationSys'],

    ['ManufaEngineering'],

    ['Marketing'],

    ['MechaEngineering'],

    ['TeleCom'],

    ['TV Production'],

    ['UrbanDesign']]


@client.command()
async def course(ctx,*,roleIN):

    #algo to find closest string to input
    roleOUT = process.extract(roleIN, courseRoles, limit=5)

    #saves closest string to roleVAR
    roleVAR = roleOUT[0][0][0]

    #gets role from server based on roleVAR
    x = discord.utils.get(ctx.guild.roles, name=roleVAR)
    m_role = []

    #takes all roles from author and puts in on a list
    for mem_role in ctx.author.roles:
        m_role.append(mem_role)

    #compares courseRoles to author's roles and removes any existing course roles
    for _ in courseRoles:
        for i in m_role:
            if i.name == _[0] and i != x:
                await ctx.author.remove_roles(i)

    #TODO: add embed
    embed=discord.Embed(title="Course Roles", description= f"Results for \"{roleIN}\" :", color=0x1271c4)

    count = 0

    #list to refer to discord number emote
    numdict = ((0,':zero:'),(1,':one:'), (2, ':two:'),(3,':three:'),(4,':four:'),(5,':five:'),

               (6,':six:'),(7,':seven:'),(8,':eight:'),(9,':nine'))
    for roleOut in roleOUT: #roleOut example: (['BioInformatics'], 90)

        if roleOut[1] > 60:
            count += 1
            embed.add_field(name = "\u200b", value = f'{numdict[count][1]} - {roleOut[0][0]}' ,inline = True)

    justSent = await ctx.send(embed=embed)

    #TODO: add reaction role on embed
    for i in range(1):
        await justSent.add_reaction(f"1️⃣")

    #TODO: make reaction give author select role

    #TODO: modify embed message, remove all reactions

    #TBD: gives author the role
    await ctx.author.add_roles(x)
    await ctx.send(f"Role {roleVAR} given ;)")




@client.command()
async def embedtest(ctx):
    roleIN = "hi"
    embed = discord.Embed(title=f'Results for \"{roleIN}\"')


    embed.add_field(value = ctx.author.id, inline = True)
    await ctx.send(embed=embed)



'''@client.command()
async def role(ctx,*,role):
    r=[]
    for a in ctx.guild.roles:
        r.append(a.name)
    if role in r:
        x=discord.utils.get(ctx.guild.roles,name=role)
    elif role not in r:
        x=await ctx.guild.create_role(name=role)
    await ctx.member.add_roles(x)
'''
#--------------------------------------------------------
client.run('NzU5MDA2OTE4NTYyOTM4ODkx.X23ORw.byOspn9OpCpywwY7MbkhU0EwsJM')

"NzU5MDA2OTE4NTYyOTM4ODkx.X23ORw.byOspn9OpCpywwY7MbkhU0EwsJM" #real bot
"NzU5NzE0NzgyMDU5NTYwOTgw.X3Bhhg.NyOghAJIG1M70qTpNH7OExpn7xY" #test bot