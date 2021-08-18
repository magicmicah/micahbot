import discord
import micahbot_functions
import settings

client = discord.Client()

@client.event
async def on_ready(self):
    print(f"We have logged in as {self.user}.")

@client.event
async def on_message(self, message):
    if message.author == self.user or message.author.bot:
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
        response = f"Hey there ${mention} - ${my_message}"
        await message.channel.send(response)

client.run(settings.DISCORD_BOT_TOKEN)
