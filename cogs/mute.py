from datetime import timedelta
import disnake
from disnake.ext import commands


class MuteCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(description="Mute a specified member with an optional reason")
    async def mute(self, ctx, member: disnake.Member, *, reason="Unspecified reason", days=0, hours=1, minutes=0, seconds=0):
        if member.id == ctx.author.id:
            await ctx.send("You cannot mute yourself, sorry! :)")
            return
        elif member.top_role >= ctx.author.top_role:
            await ctx.send(f"You can only moderate members below your role")
            return
        else:
            duration = timedelta(days=days, hours=hours,
                                 minutes=minutes, seconds=seconds)
            await member.timeout(reason=reason, duration=duration)
            reasonEmbed = disnake.Embed(
                title="User Muted",
                description=f'Succesfully muted {member.mention} for {reason} for {days} days, {hours} hours, {minutes} minutes, {seconds} seconds\n \n ',
                colour=0xFF0000
            )
            reasonEmbed.set_author(
                name=f"{member.name}" + "#" + f"{member.discriminator}", icon_url='{}'.format(member.display_avatar))
            reasonEmbed.set_footer(
                text=f"Muted by {ctx.author.name}", icon_url='{}'.format(ctx.author.avatar))
            reasonEmbed.set_thumbnail(url=member.display_avatar)
            await ctx.send(embed=reasonEmbed)


def setup(bot: commands.Bot):
    bot.add_cog(MuteCommand(bot))
