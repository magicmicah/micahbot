import discord
import micahbot_functions
import settings

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!dadjoke'):
        dadjoke = micahbot_functions.get_dadjoke()
        await message.channel.send(dadjoke)
    if message.content.startswith('!startupidea'):
        idea = micahbot_functions.get_startup_idea()
        await message.channel.send(idea)
    if message.content.startswith('!report'):
        report = micahbot_functions.report_message()
        await message.channel.send(report)
client.run(settings.DISCORD_BOT_TOKEN)
