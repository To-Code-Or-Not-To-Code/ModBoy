import disnake
from disnake.ext import commands

class KickCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(description="Kicks a specified member with an optional reason")
    async def kick(self, ctx, member: disnake.Member, *, reason="Unspecified reason"):
        if member.id == ctx.author.id:
            await ctx.send("You cannot kick yourself, sorry! :)")
            return
        elif member.top_role >= ctx.author.top_role:
            await ctx.send(f"You can only moderate members below your role")
            return
        else:
            await member.kick(reason=reason)
            reasonEmbed = disnake.Embed(
                title="User Kicked",
                description=f'Succesfully kicked {member.mention} for {reason}\n \n ',
                colour=0xFF0000
            )
            reasonEmbed.set_author(
                name=f"{member.name}" + "#" + f"{member.discriminator}", icon_url='{}'.format(member.display_avatar))
            reasonEmbed.set_footer(
                text=f"Kicked by {ctx.author.name}", icon_url='{}'.format(ctx.author.avatar))
            reasonEmbed.set_thumbnail(url=member.display_avatar)
            await ctx.send(embed=reasonEmbed)  
            
def setup(bot: commands.Bot):
    bot.add_cog(KickCommand(bot))