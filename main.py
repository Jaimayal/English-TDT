import discord
import os
from dotenv import load_dotenv
import paragraphReader

load_dotenv()
bot = discord.Bot(debug_guilds=[])


@bot.event
async def on_ready():
    print(f"{bot.user}")


@bot.slash_command(name="c1", description="Extracto de texto nivel C1 - Avanzado")
async def c1_level(ctx):
    embed = await get_embed('C1')
    await ctx.respond("Here's your Paragraph", embed=embed)


@bot.slash_command(name="b2", description="Extracto de texto nivel B2 - Intermedio Avanzado")
async def c2_level(ctx):
    embed = await get_embed('B2')
    await ctx.respond("Here's your Paragraph", embed=embed)


@bot.slash_command(name="b1", description="Extracto de texto nivel B1 - Intermedio")
async def b1_level(ctx):
    embed = await get_embed('B1')
    await ctx.respond("Here's your Paragraph", embed=embed)


@bot.slash_command(name="a2", description="Extracto de texto nivel A2 - Elemental")
async def a2_level(ctx):
    embed = await get_embed('A2')
    await ctx.respond("Here's your Paragraph", embed=embed)


@bot.slash_command(name="a1", description="Extracto de texto nivel A1 - Principiante")
async def a1_level(ctx):
    embed = await get_embed('A1')
    await ctx.respond("Here's your Paragraph", embed=embed)


async def get_embed(level):
    embed = discord.Embed(
        color=discord.Colour.blurple(),
    )
    level = level.upper()
    embed.add_field(name="*" + level + " Paragraph*", value=paragraphReader.random_paragraph(level))
    embed.set_footer(
        text="Extraido de: https://learnenglish.britishcouncil.org/skills/reading/" + level + "-reading")
    return embed


bot.run(os.getenv('TOKEN'))

