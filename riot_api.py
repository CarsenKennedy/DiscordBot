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
        self.sr_dict = dict()
        self.solo_dict = dict()
        self.tft_dict = dict()

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
        return list_of_stats

    def check_solo_rank(self):
        list_of_stats = self.get_ranked_info()
        for index in list_of_stats:
            if 'SOLO' in index['queueType']:
                tier = index['tier']
                if 'IRON' in tier:
                    rank = 'Iron' + ' ' + index['rank'] + ' ' + str(index['leaguePoints']) + ' ' + 'LP'
                    self.solo_dict['wins'] = index['wins']
                    self.solo_dict['losses'] = index['losses']
                    self.solo_dict['solo'] = rank
                    pic = "https://vignette.wikia.nocookie.net/leagueoflegends/images/0/03/Season_2019_-_Iron_1.png/revision/latest?cb=20181229234926"
                    self.solo_dict['url'] = pic
                elif 'BRONZE' in tier:
                    rank = 'Bronze' + ' ' + index['rank'] + ' ' + str(index['leaguePoints']) + ' ' + 'LP'
                    self.solo_dict['wins'] = index['wins']
                    self.solo_dict['losses'] = index['losses']
                    self.solo_dict['solo'] = rank
                    pic = "https://vignette.wikia.nocookie.net/leagueoflegends/images/f/f4/Season_2019_-_Bronze_1.png/revision/latest?cb=20181229234910"
                    self.solo_dict['url'] = pic
                elif 'SILVER' in tier:
                    rank = 'Silver' + ' ' + index['rank'] + ' ' + str(index['leaguePoints']) + ' ' + 'LP'
                    self.solo_dict['wins'] = index['wins']
                    self.solo_dict['losses'] = index['losses']
                    self.solo_dict['solo'] = rank
                    pic = "https://vignette.wikia.nocookie.net/leagueoflegends/images/7/70/Season_2019_-_Silver_1.png/revision/latest?cb=20181229234936"
                    self.solo_dict['url'] = pic
                elif 'GOLD' in tier:
                    rank = 'Gold' + ' ' + index['rank'] + ' ' + str(index['leaguePoints']) + ' ' + 'LP'
                    self.solo_dict['wins'] = index['wins']
                    self.solo_dict['losses'] = index['losses']
                    self.solo_dict['solo'] = rank
                    pic = "https://vignette.wikia.nocookie.net/leagueoflegends/images/9/96/Season_2019_-_Gold_1.png/revision/latest?cb=20181229234920"
                    self.solo_dict['url'] = pic
                elif 'PLATINUM' in tier:
                    rank = 'Platinum' + ' ' + index['rank'] + ' ' + str(index['leaguePoints']) + ' ' + 'LP'
                    self.solo_dict['wins'] = index['wins']
                    self.solo_dict['losses'] = index['losses']
                    self.solo_dict['solo'] = rank
                    pic = "https://vignette.wikia.nocookie.net/leagueoflegends/images/7/74/Season_2019_-_Platinum_1.png/revision/latest?cb=20181229234932"
                    self.solo_dict['url'] = pic
                elif 'DIAMOND' in tier:
                    rank = 'Diamond' + ' ' + index['rank'] + ' ' + str(index['leaguePoints']) + ' ' + 'LP'
                    self.solo_dict['wins'] = index['wins']
                    self.solo_dict['losses'] = index['losses']
                    self.solo_dict['solo'] = rank
                    pic = "https://vignette.wikia.nocookie.net/leagueoflegends/images/9/91/Season_2019_-_Diamond_1.png/revision/latest?cb=20181229234917"
                    self.solo_dict['url'] = pic
                elif 'MASTER' in tier:
                    rank = 'Master' + ' ' + index['rank'] + ' ' + str(index['leaguePoints']) + ' ' + 'LP'
                    self.solo_dict['wins'] = index['wins']
                    self.solo_dict['losses'] = index['losses']
                    self.solo_dict['solo'] = rank
                    pic = "https://vignette.wikia.nocookie.net/leagueoflegends/images/1/11/Season_2019_-_Master_1.png/revision/latest?cb=20181229234929"
                    self.solo_dict['url'] = pic
                elif 'GRANDMASTER' in tier:
                    rank = 'Grandmaster' + ' ' + index['rank'] + ' ' + str(index['leaguePoints']) + ' ' + 'LP'
                    self.solo_dict['wins'] = index['wins']
                    self.solo_dict['losses'] = index['losses']
                    self.solo_dict['solo'] = rank
                    pic = "https://vignette.wikia.nocookie.net/leagueoflegends/images/7/76/Season_2019_-_Grandmaster_1.png/revision/latest?cb=20181229234923"
                    self.solo_dict['url'] = pic
                elif 'CHALLENGER' in tier:
                    rank = 'Challenger' + ' ' + index['rank'] + ' ' + str(index['leaguePoints']) + ' ' + 'LP'
                    self.solo_dict['wins'] = index['wins']
                    self.solo_dict['losses'] = index['losses']
                    self.solo_dict['solo'] = rank
                    pic = "https://vignette.wikia.nocookie.net/leagueoflegends/images/5/5f/Season_2019_-_Challenger_1.png/revision/latest?cb=20181229234913"
                    self.solo_dict['url'] = pic
                else:
                    return None

    def check_tft_rank(self):
        list_of_stats = self.get_ranked_info()
        for index in list_of_stats:
            if 'TFT' in index['queueType']:
                tier = index['tier']
                if 'IRON' in tier:
                    rank = 'Iron' + ' ' + index['rank'] + ' ' + str(index['leaguePoints']) + ' ' + 'LP'
                    self.tft_dict['wins'] = index['wins']
                    self.tft_dict['losses'] = index['losses']
                    self.tft_dict['TFT'] = rank
                    pic = "https://vignette.wikia.nocookie.net/leagueoflegends/images/0/03/Season_2019_-_Iron_1.png/revision/latest?cb=20181229234926"
                    self.tft_dict['url'] = pic
                elif 'BRONZE' in tier:
                    rank = 'Bronze' + ' ' + index['rank'] + ' ' + str(index['leaguePoints']) + ' ' + 'LP'
                    self.tft_dict['wins'] = index['wins']
                    self.tft_dict['losses'] = index['losses']
                    self.tft_dict['TFT'] = rank
                    pic = "https://vignette.wikia.nocookie.net/leagueoflegends/images/f/f4/Season_2019_-_Bronze_1.png/revision/latest?cb=20181229234910"
                    self.tft_dict['url'] = pic
                elif 'SILVER' in tier:
                    rank = 'Silver' + ' ' + index['rank'] + ' ' + str(index['leaguePoints']) + ' ' + 'LP'
                    self.tft_dict['wins'] = index['wins']
                    self.tft_dict['losses'] = index['losses']
                    self.tft_dict['TFT'] = rank
                    pic = "https://vignette.wikia.nocookie.net/leagueoflegends/images/7/70/Season_2019_-_Silver_1.png/revision/latest?cb=20181229234936"
                    self.tft_dict['url'] = pic
                elif 'GOLD' in tier:
                    rank = 'Gold' + ' ' + index['rank'] + ' ' + str(index['leaguePoints']) + ' ' + 'LP'
                    self.tft_dict['wins'] = index['wins']
                    self.tft_dict['losses'] = index['losses']
                    self.tft_dict['TFT'] = rank
                    pic = "https://vignette.wikia.nocookie.net/leagueoflegends/images/9/96/Season_2019_-_Gold_1.png/revision/latest?cb=20181229234920"
                    self.tft_dict['url'] = pic
                elif 'PLATINUM' in tier:
                    rank = 'Platinum' + ' ' + index['rank'] + ' ' + str(index['leaguePoints']) + ' ' + 'LP'
                    self.tft_dict['wins'] = index['wins']
                    self.tft_dict['losses'] = index['losses']
                    self.tft_dict['TFT'] = rank
                    pic = "https://vignette.wikia.nocookie.net/leagueoflegends/images/7/74/Season_2019_-_Platinum_1.png/revision/latest?cb=20181229234932"
                    self.tft_dict['url'] = pic
                elif 'DIAMOND' in tier:
                    rank = 'Diamond' + ' ' + index['rank'] + ' ' + str(index['leaguePoints']) + ' ' + 'LP'
                    self.tft_dict['wins'] = index['wins']
                    self.tft_dict['losses'] = index['losses']
                    self.tft_dict['TFT'] = rank
                    pic = "https://vignette.wikia.nocookie.net/leagueoflegends/images/9/91/Season_2019_-_Diamond_1.png/revision/latest?cb=20181229234917"
                    self.tft_dict['url'] = pic
                elif 'MASTER' in tier:
                    rank = 'Master' + ' ' + index['rank'] + ' ' + str(index['leaguePoints']) + ' ' + 'LP'
                    self.tft_dict['wins'] = index['wins']
                    self.tft_dict['losses'] = index['losses']
                    self.tft_dict['TFT'] = rank
                    pic = "https://vignette.wikia.nocookie.net/leagueoflegends/images/1/11/Season_2019_-_Master_1.png/revision/latest?cb=20181229234929"
                    self.tft_dict['url'] = pic
                elif 'GRANDMASTER' in tier:
                    rank = 'Grandmaster' + ' ' + index['rank'] + ' ' + str(index['leaguePoints']) + ' ' + 'LP'
                    self.tft_dict['wins'] = index['wins']
                    self.tft_dict['losses'] = index['losses']
                    self.tft_dict['TFT'] = rank
                    pic = "https://vignette.wikia.nocookie.net/leagueoflegends/images/7/76/Season_2019_-_Grandmaster_1.png/revision/latest?cb=20181229234923"
                    self.tft_dict['url'] = pic
                elif 'CHALLENGER' in tier:
                    rank = 'Challenger' + ' ' + index['rank'] + ' ' + str(index['leaguePoints']) + ' ' + 'LP'
                    self.tft_dict['wins'] = index['wins']
                    self.tft_dict['losses'] = index['losses']
                    self.tft_dict['TFT'] = rank
                    pic = "https://vignette.wikia.nocookie.net/leagueoflegends/images/5/5f/Season_2019_-_Challenger_1.png/revision/latest?cb=20181229234913"
                    self.tft_dict['url'] = pic
                else:
                    return None

    def check_flex_rank(self):
        list_of_stats = self.get_ranked_info()
        for index in list_of_stats:
            if 'FLEX_SR' in index['queueType']:
                tier = index['tier']
                if 'IRON' in tier:
                    rank = 'Iron' + ' ' + index['rank'] + ' ' + str(index['leaguePoints']) + ' ' + 'LP'
                    self.sr_dict['wins'] = index['wins']
                    self.sr_dict['losses'] = index['losses']
                    self.sr_dict['flex'] = rank
                    pic = "https://vignette.wikia.nocookie.net/leagueoflegends/images/0/03/Season_2019_-_Iron_1.png/revision/latest?cb=20181229234926"
                    self.sr_dict['url'] = pic
                elif 'BRONZE' in tier:
                    rank = 'Bronze' + ' ' + index['rank'] + ' ' + str(index['leaguePoints']) + ' ' + 'LP'
                    self.sr_dict['wins'] = index['wins']
                    self.sr_dict['losses'] = index['losses']
                    self.sr_dict['flex'] = rank
                    pic = "https://vignette.wikia.nocookie.net/leagueoflegends/images/f/f4/Season_2019_-_Bronze_1.png/revision/latest?cb=20181229234910"
                    self.sr_dict['url'] = pic
                elif 'SILVER' in tier:
                    rank = 'Silver' + ' ' + index['rank'] + ' ' + str(index['leaguePoints']) + ' ' + 'LP'
                    self.sr_dict['wins'] = index['wins']
                    self.sr_dict['losses'] = index['losses']
                    self.sr_dict['flex'] = rank
                    pic = "https://vignette.wikia.nocookie.net/leagueoflegends/images/7/70/Season_2019_-_Silver_1.png/revision/latest?cb=20181229234936"
                    self.sr_dict['url'] = pic
                elif 'GOLD' in tier:
                    rank = 'Gold' + ' ' + index['rank'] + ' ' + str(index['leaguePoints']) + ' ' + 'LP'
                    self.sr_dict['wins'] = index['wins']
                    self.sr_dict['losses'] = index['losses']
                    self.sr_dict['flex'] = rank
                    pic = "https://vignette.wikia.nocookie.net/leagueoflegends/images/9/96/Season_2019_-_Gold_1.png/revision/latest?cb=20181229234920"
                    self.sr_dict['url'] = pic
                elif 'PLATINUM' in tier:
                    rank = 'Platinum' + ' ' + index['rank'] + ' ' + str(index['leaguePoints']) + ' ' + 'LP'
                    self.sr_dict['wins'] = index['wins']
                    self.sr_dict['losses'] = index['losses']
                    self.sr_dict['flex'] = rank
                    pic = "https://vignette.wikia.nocookie.net/leagueoflegends/images/7/74/Season_2019_-_Platinum_1.png/revision/latest?cb=20181229234932"
                    self.sr_dict['url'] = pic
                elif 'DIAMOND' in tier:
                    rank = 'Diamond' + ' ' + index['rank'] + ' ' + str(index['leaguePoints']) + ' ' + 'LP'
                    self.sr_dict['wins'] = index['wins']
                    self.sr_dict['losses'] = index['losses']
                    self.sr_dict['flex'] = rank
                    pic = "https://vignette.wikia.nocookie.net/leagueoflegends/images/9/91/Season_2019_-_Diamond_1.png/revision/latest?cb=20181229234917"
                    self.sr_dict['url'] = pic
                elif 'MASTER' in tier:
                    rank = 'Master' + ' ' + index['rank'] + ' ' + str(index['leaguePoints']) + ' ' + 'LP'
                    self.sr_dict['wins'] = index['wins']
                    self.sr_dict['losses'] = index['losses']
                    self.sr_dict['flex'] = rank
                    pic = "https://vignette.wikia.nocookie.net/leagueoflegends/images/1/11/Season_2019_-_Master_1.png/revision/latest?cb=20181229234929"
                    self.sr_dict['url'] = pic
                elif 'GRANDMASTER' in tier:
                    rank = 'Grandmaster' + ' ' + index['rank'] + ' ' + str(index['leaguePoints']) + ' ' + 'LP'
                    self.sr_dict['wins'] = index['wins']
                    self.sr_dict['losses'] = index['losses']
                    self.sr_dict['flex'] = rank
                    pic = "https://vignette.wikia.nocookie.net/leagueoflegends/images/7/76/Season_2019_-_Grandmaster_1.png/revision/latest?cb=20181229234923"
                    self.sr_dict['url'] = pic
                elif 'CHALLENGER' in tier:
                    rank = 'Challenger' + ' ' + index['rank'] + ' ' + str(index['leaguePoints']) + ' ' + 'LP'
                    self.sr_dict['wins'] = index['wins']
                    self.sr_dict['losses'] = index['losses']
                    self.sr_dict['flex'] = rank
                    pic = "https://vignette.wikia.nocookie.net/leagueoflegends/images/5/5f/Season_2019_-_Challenger_1.png/revision/latest?cb=20181229234913"
                    self.sr_dict['url'] = pic
                else:
                    return None










