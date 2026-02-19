import os
import discord
from discord.ext import commands
import requests

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

def encurtar(url):
    r = requests.get("https://is.gd/create.php", params={"format": "simple", "url": url})
    return r.text

@bot.event
async def on_ready():
    print(f"✅ Logado como {bot.user}")

@bot.command()
async def encurtarlink(ctx, url: str):
    try:
        short = encurtar(url)
        await ctx.send(f"🔗 {short}")
    except:
        await ctx.send("❌ Erro
