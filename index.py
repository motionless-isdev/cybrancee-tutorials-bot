import os
import discord
from discord.ext import commands
from config import TOKEN, PREFIX

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print("Loading commands in the commands folder...")

    # Load all Cogs dynamically
    for filename in os.listdir("./commands"):
        if filename.endswith(".py"):
            try:
                await bot.load_extension(f"commands.{filename[:-3]}")
                print(f"Commands Loaded: {filename}")
            except Exception as e:
                print(f"Command Failed to load {filename}: {e}")

    # Sync slash commands
    try:
        synced = await bot.tree.sync()
        print(f"Command has been synced {len(synced)} slash command(s).")
    except Exception as e:
        print(f"Command Failed to sync commands: {e}")

    print("Bot is ready and online")

bot.run(TOKEN)
