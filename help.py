import disnake
from disnake.ext import commands

class HelpCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(description="Displays help")
    async def help(self, ctx):
        ctx.send("This is a very depressing bot that is being worked on. Made by R!(k-G1!t(|-|z.")
        ctx.send("""
        /help: shows this
        /yell: makes your message capslock
        /yellat: mentions someone before making your message capslock
        /ban: ban someone with an optional reason
        /unban: unban someone with an optional reason
        /kick: kick someone with an optional reason
        /mute or /timeout: mutes someone for a set amount of time and an optional reason
        """)
            
def setup(bot: commands.Bot):
    bot.add_cog(HelpCommand(bot))