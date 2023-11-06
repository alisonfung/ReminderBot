import discord
from discord.ext import commands, tasks
import settings
import random
import asyncio

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
        return msg.channel == ctx.channel

    msg = await bot.wait_for('message', check=check)
    await ctx.channel.send(f'You sent: {msg.content}')
    
# run the bot
bot.run(settings.DISCORD_API_SECRET)



