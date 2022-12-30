import disnake
import os
from disnake.ext import commands
from dotenv import load_dotenv

load_dotenv("secrets.env")

intents = disnake.Intents.default()
intents.presences = True
intents.members = True
intents.message_content = True

class CustomBot(commands.Bot):
    def __init__(self):
        intents = disnake.Intents.default()
        intents.presences = True
        intents.members = True
        intents.message_content = True
        super().__init__(command_prefix=["/", ";", "|"], intents=intents, activity=disnake.Game("/help"), reload=True)
    
    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")

bot = CustomBot()

bot.load_extensions("plugins")

bot.run(os.environ["token"])
