import requests
import json
import unittest
import discord

# Assumed that players searched are from North America server
# Add own Riot API key
api = open("api_key.txt", "r").read().rstrip()


class User:
    def get_summoner_id(self):
        # Expires: Fri, Aug 16th, 2019
        url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + self.name + "?api_key=" + api
        response = requests.get(url)
        if response.status_code == 200:
            pass
        elif response.status_code == 403:
            print('Change API key')
        elif response.status_code == 404:
            print('404 Error')
            return
        else:
            print(response.status_code)
        account_ids = response.json()
        return account_ids['id']

    def __init__(self, summoner_name):
        self.name = summoner_name

    def get_ranked_info(self):
        summoner_id = self.get_summoner_id()
        url = 'https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/' + summoner_id + '?api_key=' + api
        response = requests.get(url)
        if response.status_code == 200:
            pass
        elif response.status_code == 403:
            print('Change API key')
        elif response.status_code == 404:
            print('404 Error')
        else:
            print(response.status_code)
        list_of_stats = response.json()
        return print(list_of_stats)

# TODO: Check rank from json object and return rank

    def check_rank(self):
        list_of_stats = self.get_ranked_info()
        for index in list_of_stats:
            if 'SR' in index['queueType']:
                tier = index['tier']
                if 'BRONZE' in tier:
                    embed = discord.Embed(title=f'{d.name}', description='Solo/Duo' + {tier}, color=0x00ff00)
                    embed.set_thumbnail(url="attachment://bronze.png")
                elif 'SILVER' in tier:
                    embed = discord.Embed(title=f'{d.name}', description='Solo/Duo' + {tier}, color=0x00ff00)
                    embed.set_thumbnail(url="attachment://silver.png")
                elif 'GOLD' in tier:
                    embed = discord.Embed(title=f'{d.name}', description='Solo/Duo' + {tier}, color=0x00ff00)
                    embed.set_thumbnail(url="attachment://gold.png")
                elif 'PLATINUM' in tier:
                    embed = discord.Embed(title=f'{d.name}', description='Solo/Duo' + {tier}, color=0x00ff00)
                    embed.set_thumbnail(url="attachment://platinum.png")
                elif 'DIAMOND' in tier:
                    embed = discord.Embed(title=f'{d.name}', description='Solo/Duo' + {tier}, color=0x00ff00)
                    embed.set_thumbnail(url="attachment://diamond.png")
                elif 'MASTER' in tier:
                    embed = discord.Embed(title=f'{d.name}', description='Solo/Duo' + {tier}, color=0x00ff00)
                    embed.set_thumbnail(url="attachment://master.png")
                elif 'GRANDMASTER' in tier:
                    embed = discord.Embed(title=f'{d.name}', description='Solo/Duo' + {tier}, color=0x00ff00)
                    embed.set_thumbnail(url="attachment://grandmaster.png")
                elif 'CHALLENGER' in tier:
                    embed = discord.Embed(title=f'{d.name}', description='Solo/Duo' + {tier}, color=0x00ff00)
                    embed.set_thumbnail(url="attachment://challenger.png")
            if 'SR' in index['queueType']:
                tier = index['tier']
                if 'BRONZE' in tier:
                    embed = discord.Embed(title=f'{d.name}', description='Solo/Duo' + {tier}, color=0x00ff00)
                    embed.set_thumbnail(url="attachment://bronze.png")
                elif 'SILVER' in tier:
                    embed = discord.Embed(title=f'{d.name}', description='Solo/Duo' + {tier}, color=0x00ff00)
                    embed.set_thumbnail(url="attachment://silver.png")
                elif 'GOLD' in tier:
                    embed = discord.Embed(title=f'{d.name}', description='Solo/Duo' + {tier}, color=0x00ff00)
                    embed.set_thumbnail(url="attachment://gold.png")
                elif 'PLATINUM' in tier:
                    embed = discord.Embed(title=f'{d.name}', description='Solo/Duo' + {tier}, color=0x00ff00)
                    embed.set_thumbnail(url="attachment://platinum.png")
                elif 'DIAMOND' in tier:
                    embed = discord.Embed(title=f'{d.name}', description='Solo/Duo' + {tier}, color=0x00ff00)
                    embed.set_thumbnail(url="attachment://diamond.png")
                elif 'MASTER' in tier:
                    embed = discord.Embed(title=f'{d.name}', description='Solo/Duo' + {tier}, color=0x00ff00)
                    embed.set_thumbnail(url="attachment://master.png")
                elif 'GRANDMASTER' in tier:
                    embed = discord.Embed(title=f'{d.name}', description='Solo/Duo' + {tier}, color=0x00ff00)
                    embed.set_thumbnail(url="attachment://grandmaster.png")
                elif 'CHALLENGER' in tier:
                    embed = discord.Embed(title=f'{d.name}', description='Solo/Duo' + {tier}, color=0x00ff00)
                    embed.set_thumbnail(url="attachment://challenger.png")


# Quick tests

d = User('Ina')
d.get_ranked_info()
d.check_rank()




