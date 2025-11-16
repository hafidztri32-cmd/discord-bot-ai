import os
import discord
from discord.ext import commands
from gpt4all import GPT4All
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# Load GPT4All offline model (versi 0.1.7 compatible ARM)
gpt_model = GPT4All("gpt4all-model.bin")

@bot.event
async def on_ready():
    print(f"Bot online sebagai {bot.user}")

@bot.command()
async def ai(ctx, *, prompt):
    msg = await ctx.send("⏳ Sedang memikirkan jawaban...")
    try:
        response = gpt_model.generate(prompt, max_tokens=200)
        await msg.edit(content=response)
    except Exception as e:
        await msg.edit(content=f"❌ Error: {e}")

bot.run(DISCORD_TOKEN)
