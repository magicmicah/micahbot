import discord
import eventloop
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

    await eventloop.eventloop(message, client)

client.run(settings.DISCORD_BOT_TOKEN)

@bot.command(aliases=["myartdegree"])
async def stable_diffusion(ctx, *, prompt):
    """Generate an image from a text prompt using the stable-diffusion model"""
    msg = await ctx.send(f"“{prompt}”\n> Generating...")

    model = replicate.models.get("stability-ai/stable-diffusion")
    image = model.predict(prompt=prompt)[0]

    await msg.edit(content=f"“{prompt}”\n{image}")

@bot.command(aliases=["whosthatpokemon"])
async def whos_that_pokemon(ctx, *, prompt):
    """Generate an image from a text prompt using the stable-diffusion model"""
    msg = await ctx.send(f"“{prompt}”\n> Generating...")

    model = replicate.models.get("lambdal/text-to-pokemon")
    image = model.predict(prompt=prompt)[0]

    await msg.edit(content=f"“{prompt}”\n{image}")

@bot.command(aliases=["minidalle"])
async def mini_dalle(ctx, *, prompt):
    """Generate an image from a text prompt using the stable-diffusion model"""
    msg = await ctx.send(f"“{prompt}”\n> Generating...")

    model = replicate.models.get("kuprel/min-dalle")
    image = model.predict(text=prompt)[0]

    await msg.edit(content=f"“{prompt}”\n{image}")

@bot.command(aliases=["funkopop"])
async def funko_pop(ctx, *, prompt):
    """Generate an image from a text prompt using the stable-diffusion model"""
    msg = await ctx.send(f"“{prompt}”\n> Generating a new Funko Pop...")

    model = replicate.models.get("prompthero/funko-diffusion")
    modified_prompt = f"funko style of {prompt}"
    image = model.predict(prompt=modified_prompt)[0]

    await msg.edit(content=f"“{prompt}”\n{image}")

@bot.command(aliases=["eldenring"])
async def elden_ring(ctx, *, prompt):
    """Generate an image from a text prompt using the stable-diffusion model"""
    msg = await ctx.send(f"“{prompt}”\n> Arise, tarnished...")
    modified_prompt = f"elden ring style, {prompt}"
    model = replicate.models.get("cjwbw/elden-ring-diffusion")
    image = model.predict(prompt=modified_prompt)[0]

    await msg.edit(content=f"“{prompt}”\n{image}")


@bot.command(aliases=["explaincode"])
async def explain_code(ctx, *, prompt):
    pass
