import discord
from discord.ext import commands
import urllib.phrase, urllib.request, re

TOKEN = 'NTUxMjA0Mjc3NjI5MjIyOTIz.D1tk6A.cp5rYne40_kZ8R6d1kUkDLcTHTQ'

client = commands.Bot(command_prefix = '-')
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='With Commands Prefix [-]'))
    print('Bots Online, Ready to help')
    
@client.event
async def on_member_join(member):
    if member.server.id == '551116302237040661':
        channel = client.get_channel('551116302891221023')
        await client.send_message(channel, f'Welcome! {member.mention} to **Byte Development**')
        
@client.event
async def on_member_remove(member):
    if member.server.id == '551116302237040661':
        channel = client.get_channel('551116302891221023')
        await client.send_message(channel, f'Bye! {member.name} :wave:')

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.purple()
    )

    embed.set_author(name='Byte Bot Info - Prefix [-]')
    embed.add_field(name='Moderation', value='-kick -ban -mute -purge -warn', inline=False)
    embed.add_field(name='Fun', value='-ping -meme(Disabled)', inline=False)
    embed.add_field(name='Info', value='-userinfo -serverinfo', inline=False)
    embed.add_field(name='Role', value='-role -rank', inline=False)
    embed.add_field(name='Search Engines', value='-youtube', inline=False)
    embed.add_field(name='Support Server', value='https://discord.gg/2S9jtAj', inline=False)
    embed.add_field(name='Creator', value='Jay_Nub#8143', inline=False)

    await client.send_message(author, embed=embed)
    await client.say('Messages sent to your Dms! :thumbsup:')

@client.command(pass_context = True)
async def purge(ctx, amount=10):
    channel = ctx.message.channel
    message = []
    msg_amount = 0
    async for message in client.logs_from(channel, limit=int(amount)):
        message.append(message)
        msg_amount += 1
    await client.delete_messages(messages)
    await client.say('{} messages deleted', format(msg_amount))
    
@client.command(pass_context=True)
async def mute(ctx,target:discord.Member):
    role=discord.utils.get(ctx.message.server.roles,name='Muted')
   
    await client.add_roles(target,role)
   
@client.command(pass_context=True)
async def warn(ctx,target:discord.Member):
    await client.send_message(target,'You have been warned!')
   
@client.command(pass_context=True)
async def kick(ctx,target:discord.Member):
    await client.kick(target)
   
@client.command(pass_context=True)
async def ban(ctx,target:discord.Member):
    await client.ban(target)    

@client.command()
async def youtube(ctx, *, search):
    
    query_string = urllib.phrase.urlencode({
        'search_query': search
    })
    hta_content = urllib.request.urlopen(
        'http://www.youtube.com/results?' + query_string
    )
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', hta_content.read().decode())
    await ctx.send('http://www.youtube.com/watch?v=' + search_results[0])
    
client.run(TOKEN)
    
