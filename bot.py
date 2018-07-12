import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk
import time

bot = commands.Bot(command_prefix='#')
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='Made By Niko#7360'))
    print ("Ready when you are xd")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.orange()
    )

    embed.set_author(name='help')
    embed.add_field(name='clear', value='Clear messages', inline=False)
    embed.add_field(name='kick', value='kick player from your server', inline=False)
    embed.add_field(name='info', value='info (playername) show u the player info', inline=False)
    embed.add_field(name='serverinfo', value='show u the server info', inline=False)

    await bot.send_message(author, embed=embed)

@bot.command(pass_context=True)
async def clear(ctx, amount=100):
    if "446740453375868939" in [role.id for role in ctx.message.author.roles]:
        channel = ctx.message.channel
        messages = []
        async for message in bot.logs_from(channel, limit=int(amount) + 1):
            messages.append(message)
        await bot.delete_messages(messages)
        await bot.say('Messages Deleted')
    else:
        await bot.say("Hey you don't have permission to use this command")

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: ping!! xSSS")
    print ("user has pinged")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("The users name is: {}".format(user.name))
    await bot.say("The users ID is: {}".format(user.id))
    await bot.say("The users status is: {}".format(user.status))
    await bot.say("The users highest role is: {}".format(user.top_role))
    await bot.say("The user joined at: {}".format(user.joined_at))

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    if "446743875617292288" in [role.id for role in ctx.message.author.roles]:
     await bot.say(" {} Has been kicked!".format(user.mention))
     await bot.send_message(user, "You have been kicked from {}.".format(ctx.message.server.name))
     await bot.kick(user)
    else:
        await bot.say("Hey you don't have permission to use this command")

@bot.command(pass_context = True)
async def say(ctx, *args):
    mesg = ' '.join(args)
    await bot.delete_message(ctx.message)
    return await bot.say(mesg)

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0x00ff00)
    embed.set_author(name="SERVER INFO")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name='Owner', value=ctx.message.server.owner, inline=False)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def Mamamia(ctx):
    await bot.say("Hi There!")
    time.sleep(2)
    for i in range (0,100000000000000000000000000000000000000000000000000000000000000000000000):
        await bot.say("Niko is best\nNiko is best\nNiko is best")
  
bot.run(os.environ['BOT_TOKEN'])
