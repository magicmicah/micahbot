from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv
import openai

from command_logs import CommandLog
import db
import settings
import micahbot_functions as MF
import session

load_dotenv()

db = db.DB(settings.SQLITE_DB_FILE)
openai.api_key = settings.OPENAI_API_KEY


intents = Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!micahbot",
    description="Runs crazy amount of stuff!",
    intents=intents,
)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if bot.user in message.mentions:
        
        
        # msg = message.content
        print(message.clean_content)

        async with message.channel.typing():

            # # Get the last command from the user
            # last_command = CommandLog.get_last_command(message.author.id)
            # last_response = CommandLog.get_last_response(message.author.id)
            # if(last_command is None):
            #     last_command = ""
            # if(last_response is None):
            #     last_response = ""
            
            # previous_conversation = last_command + "\n" + last_response
            clean_message = message.clean_content.replace(f"@MicahBot", "").strip() + " 123!@#" # Add some random characters to the end to make sure the model doesn't just repeat the prompt
            prompt = f"{clean_message}\n"
            response = MF.get_openai_completion(prompt=prompt,
            model="text-davinci-003",
            max_tokens=4000,
            temperature=0.5,
            top_p=1,
            presence_penalty=0.6,
            frequency_penalty=0.0,
            stop=["123!@#"])

            if(response is None):
                final_response = "I don't know what to say to that."
            else:
                final_response = response

            msg = await message.channel.send(final_response)
            
            user_id = message.author.id

            #CommandLog(user_id, clean_message.replace("123!@#", ""), response)
            # CommandLog(user_id, "next log", "next response")

    await bot.process_commands(message)

bot.run(settings.DISCORD_BOT_TOKEN)