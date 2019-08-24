import discord
import random
from discord.ext import commands
from riot_api import *

# Your own discord bot token goes here
Token = open("token.txt", "r").read().rstrip()

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print('Bot is ready')


@client.event
async def on_member_join(member):
    await member.send(f'{member} has joined this server.')


@client.event
async def on_member_remove(member):
    print(f'{member} has left.')


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency*1000)}ms')


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                 'It is decidedly so.',
                 'Without a doubt.',
                 'Yes - definitely.',
                 'You may rely on it.',
                 'As I see it, yes.',
                 'Most likely',
                 'Outlook good.',
                 'Yes.',
                 'Signs point to yes.',
                 'Reply hazy, try again',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 "Don't count on it.",
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Very doubtful.'
                 ]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@client.command(aliases=['lookup', 'search', 'rank'])
async def rank_lookup(ctx, summoner_name):
    d = User({summoner_name})

    # Final look of embed for .lookup
    embed = discord.Embed(title= f'{summoner_name}', url='https://na.op.gg/summoner/userName={summoner_name}', color=0x400080)
    embed.set_author(name=f"{summoner_name}", url='https://na.op.gg/summoner/userName={summoner_name}', icon_url="https://i.pinimg.com/originals/69/61/ab/6961ab1af799f02df28fa74278d78120.png%22")
    embed.set_thumbnail(url="https://i.pinimg.com/originals/69/61/ab/6961ab1af799f02df28fa74278d78120.png%22")
    embed.add_field(name= "Ranked Solo Duo", value="Rank: Master", inline=True)
    embed.add_field(name="Wins/Losses", value="256 Wins/ 456 Losses", inline=True)
    embed.add_field(name="TFT Ranked Play", value="Rank: Challenger", inline=True)
    embed.add_field(name="Wins/Losses", value="12 wins/ 118 losses", inline=True)
    embed.add_field(name="Flex 5v5", value="Rank: Gold 5", inline=True)
    embed.add_field(name="Wins/Losses", value="12 wins/18 Losses", inline=True)
    await ctx.send(embed=embed)

client.run(Token)