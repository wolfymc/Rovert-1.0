import discord
import asyncio
from discord.ext import commands

TOKEN = 'NTUxMjA0Mjc3NjI5MjIyOTIz.D1tk6A.cp5rYne40_kZ8R6d1kUkDLcTHTQ'

client = commands.Bot(command_prefix = '-')
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='With Commands Prefix = -'))
    print('Bots Online, Ready to help')

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.purple()
    )

    embed.set_author(name='Byte Bot Info - Prefix [-]')
    embed.add_field(name='Moderation', value='-kick -ban -mute -unmute -purge', inline=False)
    embed.add_field(name='Fun', value='-ping -meme(Disabled)', inline=False)
    embed.add_field(name='Info', value='-userinfo -serverinfo', inline=False)
    embed.add_field(name='Role', value='-role -rank', inline=False)
    embed.add_field(name='Support Server', value='https://discord.gg/2S9jtAj', inline=False)
    embed.add_field(name='Creator', value='Jay_Nub#8143', inline=False)

    await client.send_message(author, embed=embed)
    await client.say('Messages sent to your Dms! :thumbsup:')

@client.command(pass_context = True)
async def kick(ctx, member: discord.User):
    await client.kick(member)
    await client.delete_message(ctx.message)

@client.command(pass_context = True)
async def ban(ctx, member: discord.User):
    await client.kick(member)
    await client.delete_message(ctx.message)

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


client.run(TOKEN)
    
