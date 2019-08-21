import discord
from discord.ext import commands

Token = ''

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print('Bot is ready')



@client.event
async def on_member_join(member):
    print(f'{member} has joined this server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left.')


client.run(Token)
