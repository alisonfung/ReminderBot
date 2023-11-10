import discord
from discord.ext import commands, tasks
import settings
import random
import asyncio
from datetime import datetime, timedelta

# give discord permissions to access message content
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
# remove the library's default help command 
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def hello(ctx):
    """Says hello in response to a user."""
    await ctx.send('Hello there!')

@bot.command()
async def roll(ctx):
    """Rolls a 6-sided die and sends the result."""
    await ctx.send(str(random.randint(1, 6)))

@bot.command()
async def help(ctx):
    """DM the user a help message."""
    await ctx.author.send('This is a help message.')

@bot.command()
async def scheduleTest(ctx):
    """DM the user a scheduled message."""
    await ctx.send('You will receive a message in 10 seconds')
    await asyncio.sleep(10)
    await ctx.author.send('This is your scheduled message.')

@bot.command()
async def waitForTest(ctx):
    """Wait for the user's response and reply."""
    await ctx.send('Waiting for your next reply!')
    def check(msg):
        return msg.channel == ctx.channel and msg.author == ctx.author

    msg = await bot.wait_for('message', check=check)
    await ctx.channel.send(f'You sent: {msg.content}')
    
@bot.command()
async def reminder(ctx): 
    await ctx.send('What is the name of your reminder?') 
    def check(msg):
        return msg.channel == ctx.channel and msg.author == ctx.author 
    remindername = await bot.wait_for('message', check=check) 

    await ctx.send('In how many minutes should I remind you?') 
    def check(msg):
        return msg.channel == ctx.channel and msg.author == ctx.author 
    minutes = await bot.wait_for('message', check=check) 


    await ctx.send(f'I will remind you about {remindername.content} in {minutes.content} minutes.')
    # now= datetime.now()
    # reminder_time= now + timedelta(minutes=int(minutes.content))
    await asyncio.sleep(60*int(minutes.content)) 
    print ('60 seconds*minutes')
    print (60*int(minutes.content))

    await ctx.author.send(f'This is your scheduled reminder {remindername.content}') 


    # remindername.content it would give me the content of the message

# run the bot
bot.run(settings.DISCORD_API_SECRET) 





