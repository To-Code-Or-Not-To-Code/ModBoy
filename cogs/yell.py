import disnake
from disnake.ext import commands

class YellCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(description="Yell")
    async def yell(self, ctx, msg: str):
        if msg[len(msg) - 1] != "." and msg[len(msg) - 1] != "?":
            await ctx.send(msg.upper() + "!!!")
        else:
            await ctx.send(msg.upper().replace(".", "!!!").replace("?", "!!!"))
    
    @commands.slash_command(description="Yell at a person")
    async def yellat(self, ctx, user: str, msg: str):
        if msg[len(msg) - 1] != "." and msg[len(msg) - 1] != "?":
            await ctx.send(f"{user} {msg.upper()}!!!")
        else:
            await ctx.send(f"{user} {msg.upper().replace('.', '!!!').replace('?', '!!!')}")

def setup(bot: commands.Bot):
    bot.add_cog(YellCommands(bot))
