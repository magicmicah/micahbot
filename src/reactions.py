import discord

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


def get_gif_react(message):
    if 'mel gibson' in message.content.lower():
        return "https://giphy.com/embed/26ufoP9G2W0eOOhVu"