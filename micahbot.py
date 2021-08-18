import discord
import micahbot_functions
import settings

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user or message.author.bot:
        return

    if message.content.startswith('!dadjoke'):
        dadjoke = micahbot_functions.get_dadjoke()
        await message.channel.send(dadjoke)
    if message.content.startswith('!startupidea'):
        idea = micahbot_functions.get_startup_idea()
        await message.channel.send(idea)
    if message.content.startswith('!report'):
        my_message = micahbot_functions.report_message()
        mention = message.author.mention
        response = f"Hey there {mention} - {my_message}"
        await message.channel.send(response)
    if 'micah' in message.content.lower():
        emoji = client.get_emoji(868152784594296883)
        await message.add_reaction(emoji)
    if 'kamala' in message.content.lower():
        emoji = client.get_emoji(868149377347239986)
        await message.add_reaction(emoji)
client.run(settings.DISCORD_BOT_TOKEN)
