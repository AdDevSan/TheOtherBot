import discord
from discord.ext import commands



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

Course_Roles = [
    ['Accounting'],

    ['Actuarial',
     "Actuarial Sciences", "Actuarial Science","ActuarialScience"],

    ['Architecture'],

    ['AppMath',
     "Applied Mathematics", "App Mathematics", "AppliedMath", "AppliedMathematics", "AppMathematics"],

    ['AppChemistry',
     "Applied Chemistry", "AppChem", "AppliedChemistry"],

    ['BioInformatics',
     "Bio Informatics"],

    ['Biology',
     "Bio"],

    ['ComSci',
     "Computer Science"],

    ['Civil Engineering',
     "CivilEng", "CivilEngineering", "Civil Engineer", "CivilEngineer"],

    ['China Studies',
     "China Study", "ChinaStudies"],

    ['DigitalMedia',
     "Digital Media"],

    ['Finance',
     "EconFinance", "EconomyFinance", "Economy Finance", "Econ Finance"],

    ['Environmental Science',
     "EnviSci", "EnvironmentalScience", "Enviromental Science", "EnviromentalScience"],

    ['English'],

    ['ElectricEngineering',
     "Electrical Engineering", "ElectricalEngineering", "Electric Engineering", "ElectEng"],

    ['ItlBusiness',
     "International Business", "InternationalBusiness", "BusinessInternational", "InterBusiness"],

    ['IndustryDesign',
     "IndustrialDesign", "Industy Design", "Industrial Design", "IndusDes"],

    ['ManufaEngineering',
     "ManuEng", "Manufacturing Engineer"],

    ['MechaEngineering',
     "Mechatronic Engineering", "MechatronicEng", "MechaEng"],

    ['TeleCom',
     "Telecommunications", "Telecom Engineering", "Telecommunication Engineering"],

    ['UrbanDesign', "Urban Design", "UrbDes"]






]
@client.command()
async def course(ctx,*,roleIN):

    for _ in Course_Roles:
        for i in _:
            if roleIN.upper() == i.upper():
                roleVAR = _[0]



    x = discord.utils.get(ctx.guild.roles, name=roleVAR)
    m_role = []
    for mem_role in ctx.author.roles:
        m_role.append(mem_role)
    for _ in Course_Roles:
        for i in m_role:
            if i.name == _[0] and i != x:
                await ctx.author.remove_roles(i)

    await ctx.author.add_roles(x)
    await ctx.send(f"Role {roleVAR} given ;)")


@client.command()
@has_permissions()





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
