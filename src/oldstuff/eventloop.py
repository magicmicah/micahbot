import micahbot_functions
async def eventloop(message, client):
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
    if 'inflation' in message.content.lower():
        biden = client.get_emoji(877705553948852225)
        moneyprinter = client.get_emoji(877705040842883172)
        await message.add_reaction(biden)
        await message.add_reaction(moneyprinter)
    if 'biden' in message.content.lower():
        biden = client.get_emoji(877705553948852225)
        await message.add_reaction(biden)
    if 'trump' in message.content.lower():
        trump = client.get_emoji(877707356492935178)
        await message.add_reaction(trump)