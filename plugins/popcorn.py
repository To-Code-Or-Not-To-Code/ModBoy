import disnake
from disnake.ext import commands
import json

class PopcornCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.slash_command(description="Checks your popcorn status")
    async def popcornstatus(self, ctx, *, member=""):
        with open("popcorn.json") as file:
            popcornStuff = json.loads(file.read())
            if not member:
                member = ctx.author
            try:
                data = popcornStuff[member]
            except:
                popcornStuff[member] = 0
                data = popcornStuff[member]
            finally:
                embed = disnake.Embed(
                    title="Popcorn Status",
                    description=f"The popcorn status of {member} is: {data}"
                )
                await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(PopcornCommands(bot))