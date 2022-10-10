from datetime import timedelta
import disnake
import os
from disnake.ext import commands
from dotenv import load_dotenv

# TODO: Make mute function work #
# TODO: Add unmute and untimeout functions #
# TODO: Add unmute and untimeout embed #
# TODO: Add unban function #

load_dotenv("secrets.env")

intents = disnake.Intents.default()
intents.presences = True
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

bot.load_extensions("cogs")

bot.run(os.environ["token"])
