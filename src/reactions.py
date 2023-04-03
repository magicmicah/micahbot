import discord
import logging
import random
import requests
import settings
import urllib.parse

logger = logging.getLogger(__name__)
giphy_api_key = settings.GIPHY_API_KEY

def get_react_id(message):
    if message.guild.id == 700525223790772255:
        if 'kamala' in message.content.lower():
            kamala_imspeaking = discord.utils.get(message.guild.emojis, name='kamala_imspeaking')
            return (kamala_imspeaking,)
        if 'inflation' in message.content.lower():
            moneyprinter = discord.utils.get(message.guild.emojis, name='moneyprinter')
            scumbagjoe = discord.utils.get(message.guild.emojis, name='scumbagjoe')
            return (moneyprinter,scumbagjoe)
        if 'biden' in message.content.lower():
            scumbagjoe = discord.utils.get(message.guild.emojis, name='scumbagjoe')
            byeden = discord.utils.get(message.guild.emojis, name='byeden')
            creepyjoe = discord.utils.get(message.guild.emojis, name='creepyjoe')
            return (scumbagjoe,byeden, creepyjoe)
        if 'trump' in message.content.lower():
            trump_poggers = discord.utils.get(message.guild.emojis, name='trump_poggers')
            return (trump_poggers,)
        if 'hillary' in message.content.lower():
            killary = discord.utils.get(message.guild.emojis, name='killary')
            return (killary,)
        if 'aoc' in message.content.lower():
            aoc_laugh = discord.utils.get(message.guild.emojis, name='aoc_laugh')
            return (aoc_laugh,)
        if 'gun' in message.content.lower():
            glock = discord.utils.get(message.guild.emojis, name='glock')
            return (glock,)
    if message.guild.id == 692493756968206396:
        pass

def get_gif_react(string):
    return get_gif_by_query(string)
        #return get_random_gif('mel gibson')
        # return "https://giphy.com/embed/26ufoP9G2W0eOOhVu"

def get_random_gif(tag):
    encoded_string = urllib.parse.quote(tag)
    response = requests.get(f"https://api.giphy.com/v1/gifs/random?api_key={giphy_api_key}&tag={encoded_string}")
    if response.status_code == 200:
        return response.json()['data']['embed_url']
    else:
        return None

def get_gif_by_query(query, limit=10):
    encoded_string = urllib.parse.quote(query)
    response = requests.get(f"https://api.giphy.com/v1/gifs/search?q={encoded_string}&api_key={giphy_api_key}&limit={limit}")
    if response.status_code == 200:
        data = response.json()['data']
        if len(data) > 0:
            gif_number = random.randint(0, len(data) - 1)
            return data[gif_number]['embed_url']
        # return data['data'][0]['embed_url']
    else:
        return None