import discord
import random
import time
import asyncio
from discord.ext import commands

TOKEN = 'NTQ5Nzc5MzQxMzMzMTAyNTkz.D1o1dg.-OfFE7dM4bg1gb4CEB-TtvcaxAM'

client = commands.Bot(command_prefix = '?')
client.remove_command('help')

@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await client.send_message(server, fmt.format(member, server))

@client.event
async def on_ready():
    serverCount = len(client.servers)
    await client.change_presence(game=discord.Game(name='{} servers | ?help'.format(serverCount), type = 2, status=discord.Status.dnd))
    print('Hello')
                                                                   
@client.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(colour=discord.Colour.blue())
    embed.set_author(name="{}'s info".format(ctx.message.server.name))
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Server Owner", value=(ctx.message.server.owner))
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.add_field(name="Channels", value=len(ctx.message.server.channels))
    embed.add_field(name="Region", value=ctx.message.server.region, inline=True)
    embed.add_field(name="Server Created", value=ctx.message.server.created_at, inline=True)
    embed.add_field(name="Verification Level", value=ctx.message.server.verification_level, inline=True)
    embed.add_field(name="Is Server Large", value=ctx.message.server.large, inline=True)
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await client.say(embed=embed)
    
@client.command(pass_context=True)
async def flipcoin(ctx):
      await client.say(random.choice(['heads!', 'Tails!']))
	
@client.command(pass_context=True)
async def purge(ctx, amount=100):
	channel = ctx.message.channel
	messages = []
	async for message in client.logs_from(channel, limit=int(amount) +1):      
		message.append(message)
	await client.delete_messages(messages)
	await client.say('Messages deleted.')

@client.command(pass_context=True)
async def help(ctx):
	author = ctx.message.author
	
	embed = discord.Embed(
	           colour = discord.Colour.blue()
	)
	
	embed.set_author(name='                                      Commands')
	embed.add_field(name='Fun Commands', value='?ping <shows and returns pong> ?say <message>', inline=True)
	embed.add_field(name='Moderation Commands', value='?kick <kicks a user> ?ban <bans a user> ?clear <number of messages> ?mute <mutes user> ?unmute <unmutes user>', inline=True)
	embed.add_field(name='Info Based', value='?serverinfo <shows info on the server> ?userinfo <shows info on a server>', inline=True)
	
	await client.send_message(author, embed=embed)
	await client.say('I have sent the info in your PM')
	
@client.command(pass_context=True)
async def kick(ctx, user: discord.Member = None):
    try:
        if ctx.message.author.server_permissions.kick_members:
            if user is None:
                embed = discord.Embed(description=":no_entry_sign: **You forgot a user!**", color=(random.randint(0, 0xffffff)))
                await client.say(embed=embed)
                return
            await client.kick(user)
            embed = discord.Embed(description=f":white_check_mark:  Sucessfuly kicked **{user}**!", color=(random.randint(0, 0xffffff)))
            await client.say(embed=embed)
        else:
            embed = discord.Embed(description=":error: **You are missing KICK_MEMBERS permission.**", color=(random.randint(0, 0xffffff)))
            await client.say(embed=embed)
    except discord.Forbidden:
        embed = discord.Embed(description=":error: **I am missing permissions to use this command!**", color=(random.randint(0, 0xffffff)))
        await client.say(embed=embed)    
        
@client.command(pass_context=True)
async def ban(ctx, user: discord.Member = None):
    try:
        if ctx.message.author.server_permissions.ban_members:
            if user is None:
                embed = discord.Embed(description=":no_entry_sign: **You forgot a user!**", color=(random.randint(0, 0xffffff)))
                await client.say(embed=embed)
                return
            await client.ban(user)
            embed = discord.Embed(description=f":check: Sucessfuly banned **{user}**!", color=(random.randint(0, 0xffffff)))
            await client.say(embed=embed)
        else:
            embed = discord.Embed(description=":error: **You are missing BAN_MEMBERS permission.**", color=(random.randint(0, 0xffffff)))
            await client.say(embed=embed)
    except discord.Forbidden:
        embed = discord.Embed(description=":error: **I am missing permissions to use this command!**", color=(random.randint(0, 0xffffff)))
        await client.say(embed=embed)    
        
@client.command(pass_context=True)
async def ping(ctx):
    t = await client.say('Pong!')
    ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 1000
    await client.edit_message(t, new_content='Pong! Took: {}ms'.format(int(ms)))

@client.command(pass_context = True)
async def clear(ctx, number):
    number = int(number)
    counter = 0
    async for x in client.logs_from(ctx.message.channel, limit = number):
        if counter < number:
            await client.delete_message(x)
            counter += 1
            await asyncio.sleep(0)
        
@client.command(pass_context=True)
async def say(ctx,*msg):
	user_msg=ctx.message
	await client.say('{}'.format(' '.join(msg)))
	await asyncio.sleep()
	await client.delete_message(user_msg)

@client.command(pass_context = True)
async def mute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '518619984834854936':
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.add_roles(member, role)
        embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await client.say(embed=embed)

@client.command()
async def userinfo(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    roles = [role for role in member.roles]

    embed = discord.Embed(colour=member.colour, timestamp=ctx.message.created_at)

    embed.set_author(name=f'User Info - {member}')
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)

    embed.add_field(name='ID:', value=member.id)
    embed.add_field(name='Guild name:', value=member.display_name)

    embed.add_field(name='Created at:', value=member.created_at.strftime('%a, %#d %B %Y, %I:%M %p UTC'))
    embed.add_field(name='Joined at:', value=member.joined_at.strftime('%a, %#d %B %Y, %I:%M %p UTC'))

    embed.add_field(name=f'Roles ({len(roles)})', value=' '.join([role.mention for role in roles]))
    embed.add_field(name='Top role:', value=member.top_role.mention)

    embed.add_field(name='Bot?', value=member.bot)

    await ctx.send(embed=embed)
	
@client.command(pass_context = True)
async def invite(ctx):
	await.client.say('https://discordapp.com/api/oauth2/authorize?client_id=549779341333102593&permissions=8&scope=bot')
	
@client.command(pass_context = True)
async def supserver(ctx):
	await.client.say('https://discord.gg/pT5XRdh')

client.run(TOKEN)
