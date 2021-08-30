import asyncio
import discord
import emoji
from discord.ext import commands
from fuzzywuzzy import process



client = commands.Bot(command_prefix='$',intents=discord.Intents.all())
client.remove_command("help")
#------------------------------------------------------
#Tells if bot is ready
@client.event
async def on_ready():
	print("bot is ready...")
#------------------------------------------------------
year_roles = [759014288043671602, 759014527211143178, 759014621473538070, 759014693057855518]

#---------------------------------------------------------------------------------------------
#Year Reaction Message
Year_Message = 759024782405926952
#Year Roles
@client.event
async def on_raw_reaction_add(payload):
	if payload.message_id==Year_Message:
		m = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
		if payload.emoji.name == '1️⃣':
			role_id = year_roles[0]
			await m.remove_reaction('2️⃣', payload.member)
			await m.remove_reaction('3️⃣', payload.member)
			await m.remove_reaction('4️⃣', payload.member)
		elif payload.emoji.name=='2️⃣':
			role_id=year_roles[1]
			await m.remove_reaction('1️⃣', payload.member)
			await m.remove_reaction('3️⃣', payload.member)
			await m.remove_reaction('4️⃣', payload.member)
		elif payload.emoji.name=='3️⃣':
			role_id=year_roles[2]
			await m.remove_reaction('2️⃣', payload.member)
			await m.remove_reaction('1️⃣', payload.member)
			await m.remove_reaction('4️⃣', payload.member)
		elif payload.emoji.name=='4️⃣':
			role_id=year_roles[3]
			await m.remove_reaction('2️⃣', payload.member)
			await m.remove_reaction('3️⃣', payload.member)
			await m.remove_reaction('1️⃣', payload.member)
		r=client.get_guild(payload.guild_id).get_role(role_id)
		await payload.member.add_roles(r)

@client.event
async def on_raw_reaction_remove(payload):
	if payload.message_id==Year_Message:

		if payload.emoji.name == '1️⃣':
			role_id = year_roles[0]

		elif payload.emoji.name=='2️⃣':
			role_id=year_roles[1]

		elif payload.emoji.name=='3️⃣':
			role_id=year_roles[2]

		elif payload.emoji.name=='4️⃣':
			role_id=year_roles[3]

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
	['Accounting'],['Actuarial'],['Architecture'],['AppMath'], ['AppChemistry'], ['BioInformatics'],['Biology'],
	['BusinessAdmin'], ['ComSci'],['Communications'], ['Civil Engineering'],['China Studies'], ['DigitalMedia'], ['Finance'],
	['EconFinance'],['Environmental Science'],['English'],['ElectricalEngineering'], ['ItlBusiness'],['IndustryDesign'],
	['IntelRobotics'],['InformationSys'],['ManufaEngineering'],['Marketing'],['MechaEngineering'],['TeleCom'],
	['TV Production'],['UrbanDesign']]


@client.command()
async def course(ctx,*,roleIN):

	#algo to find closest string to input
	roleOUT = process.extract(roleIN, courseRoles, limit=5)



	# INTITIAL EMBED------------------------------------------------------------------------------
	embed=discord.Embed(title="Course Roles", description= f"results for \"{roleIN}\" :", color=0x1271c4)
	embed.set_footer(text="react to a role accordingly")
	embed.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar)
	count = 0
	#list to refer to discord number emote
	numdict = [':zero:', ':one:', ':two:', ':three:', ':four:', ':five:',

	           ':six:', ':seven:', ':eight:', ':nine']

	#EMOLIST-----------------------
	emolist = {}

	# ADDS FIELD FOR EVERY ROLE TO BE PUT IN MENU
	for roleOut in roleOUT: #roleOut example: (['BioInformatics'], 90)


		#if ratio is greater than 60 and ratio diff between first ratio and other ratio less than 25
		if roleOut[1] > 60 and (roleOUT[0][1] - roleOut[1]) <= 25:
			count += 1
			embed.add_field(name = "\u200b", value = f'{numdict[count]} - {roleOut[0][0]}' ,inline = True)
			#appends number emoji & role name to emolist
			emolist[numdict[count]] = roleOut[0][0]

	#adds cancel option if valid
	# if ratio too low: valid = false ; process ends after embed sent
	emfield = emoji.emojize(f':no_entry_sign: - Cancel Request', use_aliases = True) if emolist else 'your search was off-limits, please try again...'

	#THIS LINE SENDS THE EMBED------------------------------------------------------------------
	justSent = await ctx.send(embed=embed.add_field(name = "\u200b", value = emfield ,inline = False))

	# if valid == True
	if emolist:

		#THIS LINE PROVIDES THE REACTION ROLES BASED ON EMOLIST----------------------------------------
		for emo in emolist:
			await justSent.add_reaction(emoji.emojize(emo, use_aliases = True))

		#ADDS CANCEL BUTTON REACTION
		await justSent.add_reaction(emoji.emojize(":no_entry_sign:", use_aliases=True))

		#FROM PYTHON DISCORD SERVER
		def check(r,m):
			return m == ctx.author and r.message.channel == ctx.channel

		# removes embed desc
		editEmbed = discord.Embed(title="Course Roles", description="\u200b", color=0x1271c4)

		#try for timeout
		try:
			reaction, user = await client.wait_for('reaction_add', check=check, timeout=20) #timeout 20s

			if reaction.emoji:

				#loops through each i[0] in emolist -> [[':one:', 'BioInformatics'], [':two:','Biology']]
				mRole = ""

				#Loop to find corresponding emoji
				for i in emolist:
					#if :one:/:two:/:three: == reacted emoji
					if emoji.emojize(i, use_aliases=True) == reaction.emoji:
						#gets corresp. role name from emolist, place it in mRole variable
						mRole = emolist[i]

						#gets role from server based on name from emolist and corresp. emoji react
						matchingRole = discord.utils.get(ctx.guild.roles, name=mRole)

					#if the emoji matches role (not cancel)
				if mRole:

					#REMOVES AUTHOR EXISTING CLASS ROLES FUNCTION-----------------------------------

					# takes all roles from author to be put in m_role
					m_role = [mem_role for mem_role in ctx.author.roles]

					# compares courseRoles to author's roles and removes any existing course roles
					for _ in courseRoles:
						for i in m_role:
							if i.name == _[0]:
								await ctx.author.remove_roles(i)

					#gives author role
					await ctx.author.add_roles(matchingRole)


					# SUCCESS EMBED------------------------------------------------------------------------------------
					# edits field
					editEmbed.add_field(name=f" role \"{mRole}\" successfully added!", value='\u200b', inline=True)

				#if cancel----------------------------------------------------------------
				else:
					# edits field
					editEmbed.add_field(name=emoji.emojize("  :no_entry_sign:   Request Cancelled!",use_aliases = True), value='\u200b', inline=True)

		#TimeOut Error Response
		except asyncio.TimeoutError:

			#TIMEOUT ERROR EMBED---------------------------------------------------------------------------------
			editEmbed.add_field(name=f"TimeoutError!", value="be faster next time you slowpoke!", inline=False)
		finally:
			await justSent.edit(embed=editEmbed.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar))
			await justSent.clear_reactions()

#--------------------------------------------------------
client.run('NzU5MDA2OTE4NTYyOTM4ODkx.X23ORw.QLjkR8jXZk9Lb0lVM4XcP65CUtQ')

"NzU5MDA2OTE4NTYyOTM4ODkx.X23ORw.QLjkR8jXZk9Lb0lVM4XcP65CUtQ" #real bot
"NzU5NzE0NzgyMDU5NTYwOTgw.X3Bhhg.NyOghAJIG1M70qTpNH7OExpn7xY" #test 