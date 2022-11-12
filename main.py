import discord
from discord.ext import commands
from config import settings

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

@bot.command() 
async def hi(ctx): 
    author = ctx.message.author 

    await ctx.send(f'Скок у тебя ММР мусор не позорься выйди в окно нахуй, {author.mention}!')


bot.run(settings['TOKEN'])