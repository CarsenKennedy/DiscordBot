import discord
import random
from discord.ext import commands
from riot_api import *

# Your own discord bot token goes here
Token = open("token.txt", "r").read().rstrip()

client = commands.Bot(command_prefix='$')


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


@client.command(aliases=['lookup'])
async def rank_lookup(ctx, *, summoner_name):
    d = User(summoner_name)
    d.check_solo_rank()
    d.check_tft_rank()
    d.check_flex_rank()
    if ' ' in d.name:
        url_name = d.name.replace(' ', '+')
        embed = discord.Embed(title=f'{d.name}', url="https://na.op.gg/summoner/userName={}".format(url_name), color=0x2e64ec)
        embed.set_author(name=f"{summoner_name}", url=f'https://na.op.gg/summoner/userName={url_name}')
    else:
        embed = discord.Embed(title=f'{d.name}', url="https://na.op.gg/summoner/userName={}".format(d.name), color=0x2e64ec)
        embed.set_author(name=f"{summoner_name}", url=f'https://na.op.gg/summoner/userName={d.name}')

    if d.solo_dict.get('solo') is None and d.tft_dict.get('TFT') is None and d.sr_dict.get('flex') is None:
        embed.add_field(name='No Ranked games found', value='Play some ranked...like anything')
        # else:
        # pic = d.solo_dict["url"]
        # embed.add_field(name="Ranked Solo Duo", value=f"Rank: {d.solo_dict['solo']}", inline=True)
        # embed.add_field(name="Wins/Losses", value=f"{d.solo_dict['wins']} Wins / {d.solo_dict['losses']} Losses", inline=True)
        # if d.check_tft_rank() is None:
    elif d.solo_dict.get('solo') is not None:
        pic = d.solo_dict["url"]
        embed.set_thumbnail(url=pic)
        embed.add_field(name="Ranked Solo Duo", value=f"Rank: {d.solo_dict['solo']}", inline=True)
        embed.add_field(name="Wins/Losses", value=f"{d.solo_dict['wins']} Wins / {d.solo_dict['losses']} Losses", inline=True)
        if d.tft_dict.get('TFT') is not None:
            embed.add_field(name="TFT Ranked", value=f"Rank: {d.tft_dict['TFT']}", inline=True)
            embed.add_field(name="Wins/Losses", value=f" {d.tft_dict['wins']} wins/ {d.tft_dict['losses']} Losses",
                            inline=True)
            if d.sr_dict.get('flex') is not None:
                embed.add_field(name="Flex 5v5", value=f"Rank: {d.sr_dict['flex']}", inline=True)
                embed.add_field(name="Wins/Losses", value=f" {d.sr_dict['wins']} wins/ {d.sr_dict['losses']} Losses",
                                inline=True)
            else:
                pass
        else:
            if d.sr_dict.get('flex') is not None:
                embed.add_field(name="Flex 5v5", value=f"Rank: {d.sr_dict['flex']}", inline=True)
                embed.add_field(name="Wins/Losses", value=f" {d.sr_dict['wins']} wins/ {d.sr_dict['losses']} Losses",
                                inline=True)
            else:
                pass
    elif d.tft_dict.get('TFT') is not None:
        pic = d.tft_dict["url"]
        embed.set_thumbnail(url=pic)
        embed.add_field(name="TFT Ranked", value=f"Rank: {d.tft_dict['TFT']}", inline=True)
        embed.add_field(name="Wins/Losses", value=f" {d.tft_dict['wins']} wins/ {d.tft_dict['losses']} Losses", inline=True)
        if d.sr_dict.get()['flex'] is not None:
            embed.add_field(name="Flex 5v5", value=f"Rank: {d.sr_dict['flex']}", inline=True)
            embed.add_field(name="Wins/Losses", value=f" {d.sr_dict['wins']} wins/ {d.sr_dict['losses']} Losses",
                             inline=True)
        else:
            pass
    elif d.sr_dict.get('flex') is not None:
        pic = d.sr_dict["url"]
        embed.set_thumbnail(url=pic)
        embed.add_field(name="Flex 5v5", value=f"Rank: {d.sr_dict['flex']}", inline=True)
        embed.add_field(name="Wins/Losses", value=f" {d.sr_dict['wins']} wins/ {d.sr_dict['losses']} Losses",
                        inline=True)
    else:
        pass
        # pic = d.solo_dict["url"]
        # embed.add_field(name="Ranked Solo Duo", value=f"Rank: {d.solo_dict['solo']}", inline=True)
        # embed.add_field(name="Wins/Losses", value=f"{d.solo_dict['wins']} Wins / {d.solo_dict['losses']} Losses", inline=True)
        # embed.add_field(name="TFT Ranked", value=f"Rank: {d.tft_dict['TFT']}", inline=True)
        # embed.add_field(name="Wins/Losses", value=f" {d.tft_dict['wins']} wins/ {d.tft_dict['losses']} Losses", inline=True)
        # embed.add_field(name="Flex 5v5", value=f"Rank: {d.sr_dict['flex']}", inline=True)
        # embed.add_field(name="Wins/Losses", value=f" {d.sr_dict['wins']} wins/ {d.sr_dict['losses']} Losses", inline=True)

    await ctx.send(embed=embed)

client.run(Token)
