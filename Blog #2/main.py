import discord
from discord.ext import commands

from bot_config import bot_config 

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=bot_config.prefixes, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')
    print(f'version={bot_config.version}')

@bot.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}')
    await bot.process_commands(message)  

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

@bot.command(name='따라하기')
async def test(ctx, arg):
    await ctx.send(arg)

bot.run(bot_config.token)
