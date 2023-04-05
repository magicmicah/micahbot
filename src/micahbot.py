import discord
from discord.ext import commands
import logging
import ai
import reactions
import settings
import user
import utils

logger = logging.getLogger(__name__)
logger.info("Starting up...")

registry = user.UserRegistry()

intents = discord.Intents.all()
intents.message_content = True
intents.members = True

help_command = commands.DefaultHelpCommand(show_parameter_descriptions=False)

bot = commands.Bot(
    command_prefix="/",
    description="Micahbot is a fully featured Discord bot that does the needful things.",
    intents=intents,
    help_command=help_command,
)


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Hacking up some silliness."))
    await bot.tree.sync()
    logger.info("Micahbot is ready!")


@bot.hybrid_command(name="micahart",)
async def micahart(ctx, prompt: str = None, negative_prompt: str = None):
    """Return an image from Replicate AI based on the prompts you provide.

    Arguments:
        prompt (str, optional): The text prompt used to generate the image.
        negative_prompt (str, optional): The text prompt used to generate the image.

    Returns:
        The generated image.

    Example:
        /micahart "A beautiful sunset." "people"
        https://prompthero.com/stable-diffusion-prompts
    """
    if not prompt:
        await ctx.send("Please provide a prompt to generate an image.")
        return

    if not negative_prompt:
        msg = await ctx.send(f"Generating...")
        image = ai.get_replicate_image(prompt, negative_prompt)
        await msg.edit(content=f"Prompt: {prompt}\n{image}")
    else:
        msg = await ctx.send(f"Generating...")
        image = ai.get_replicate_image(prompt, negative_prompt)
        await msg.edit(content=f"Prompt: {prompt}\nNegative prompt: {negative_prompt}\n {image}")

@bot.event
async def on_member_join(member):
    registry.add_user(member.id, member.name)
    for channel in member.guild.channels:
        if str(channel) == "general":
            await channel.send(f"""Welcome to the server {member.mention}!""")

@bot.event
async def on_member_remove(member):
    registry.remove_user(member.id)
    for channel in member.guild.channels:
        if str(channel) == "general":
            await channel.send(f"""{member.mention} has left the server.""")

@bot.event
async def on_message(message):

    if message.channel is not None:
        react_ids = reactions.get_react_id(message)
        if react_ids is not None:
            for react_id in react_ids:
                await message.add_reaction(react_id)

    roll_dice = utils.roll_dice(1000)
    if roll_dice == 1:
        nouns = ai.get_nouns(message.content)
        noun_string = " ".join(nouns)
        gif_react = reactions.get_gif_react(noun_string)
        logger.info(f"Rolled a 1. Getting a GIF based off: {noun_string}")
        if gif_react is not None:
            await message.reply(gif_react)    

    if message.author == bot.user:
        return
    

    if bot.user in message.mentions:

        user_registered = registry.is_user_in_registry(message.author.id)
        if user_registered is False and message.author != bot.user:
            # async with message.channel.typing():
            #     await message.channel.send(f"Hello {message.author.mention}! By messaging me, you agree to abide by the terms and conditions from OpenAI (https://openai.com/policies/terms-of-use).")
            registry.add_user(message.author.id, message.author.name)
        
        clean_message = message.clean_content.replace(f"@MicahBot", "").strip()
        
        registry.append_user_message(message.author.id, "user", clean_message)

        user_messages = registry.get_user_messages(message.author.id)

        async with message.channel.typing():


            response = ai.get_openai_chat_completion(
                        model="gpt-3.5-turbo",
                        messages=user_messages,
                        user=str(message.author.id))
            
            if(response is None):
                final_response = "I don't know what to say to that."
            else:
                final_response = response
                registry.append_user_message(message.author.id, "assistant", final_response)
                #user_messages.append({"role": "assistant", "content": final_response})

            await message.channel.send(final_response)
            

    await bot.process_commands(message)

bot.run(settings.DISCORD_BOT_TOKEN)
