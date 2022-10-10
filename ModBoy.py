from datetime import timedelta
import disnake
import os
from disnake.ext import commands
from dotenv import load_dotenv

# TODO: Make mute function work #
# TODO: Add unmute and untimeout functions #
# TODO: Add unmute and untimeout embed #
# TODO: Add unban function #

load_dotenv()

intents = disnake.Intents.default()
intents.presences = True
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

def embed(ctx, member, reason, type, days=0, hours=0, minutes=0, seconds=0):
    if type == "ban":
        reasonEmbed = disnake.Embed(
            title="User Banned",
            description=f'Succesfully banned {member.mention} for {reason}\n \n ',
            colour=0xFF0000
        )
        reasonEmbed.set_author(
            name=f"{member.name}" + "#" + f"{member.discriminator}", icon_url='{}'.format(member.display_avatar))
        reasonEmbed.set_footer(
            text=f"Banned by {ctx.author.name}", icon_url='{}'.format(ctx.author.avatar))
        reasonEmbed.set_thumbnail(url=member.display_avatar)
        return reasonEmbed
    elif type == "kick":
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
        return reasonEmbed
    elif type == "unban":
        reasonEmbed = disnake.Embed(
            title="User Unbanned",
            description=f'Succesfully unbanned {member.mention} for {reason}\n \n ',
            colour=0xFF0000
        )
        reasonEmbed.set_author(
            name=f"{member.name}" + "#" + f"{member.discriminator}", icon_url='{}'.format(member.display_avatar))
        reasonEmbed.set_footer(
            text=f"Unbanned by {ctx.author.name}", icon_url='{}'.format(ctx.author.avatar))
        reasonEmbed.set_thumbnail(url=member.display_avatar)
        return
    elif type == "timeout":
        if days or hours or minutes or seconds:
            reasonEmbed = disnake.Embed(
                title="User Timedout",
                description=f'Succesfully timedout {member.mention} for {reason} for {days} days, {hours} hours, {minutes} minutes, {seconds} seconds\n \n ',
                colour=0xFF0000
            )
        else:
            reasonEmbed = disnake.Embed(
                title="User Timedout",
                description=f'Succesfully timedout {member.mention} for {reason} until untimed out\n \n ',
                colour=0xFF0000
            )
        reasonEmbed.set_author(
            name=f"{member.name}" + "#" + f"{member.discriminator}", icon_url='{}'.format(member.display_avatar))
        reasonEmbed.set_footer(
            text=f"Timedout by {ctx.author.name}", icon_url='{}'.format(ctx.author.avatar))
        reasonEmbed.set_thumbnail(url=member.display_avatar)
        return reasonEmbed
    elif type == "mute":
        reasonEmbed = disnake.Embed(
            title="User Muted",
            description=f'Succesfully muted {member.mention} for {reason}\n \n ',
            colour=0xFF0000
        )
        reasonEmbed.set_author(
            name=f"{member.name}" + "#" + f"{member.discriminator}", icon_url='{}'.format(member.display_avatar))
        reasonEmbed.set_footer(
            text=f"Muted by {ctx.author.name}", icon_url='{}'.format(ctx.author.avatar))
        reasonEmbed.set_thumbnail(url=member.display_avatar)
        return reasonEmbed
    else:
        reasonEmbed = disnake.Embed(
            title="Test",
            description=f'Test',
            colour=0xFF0000
        )
        return reasonEmbed


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@bot.slash_command(description="Makes your message capslock")
async def yell(inter, msg: str):
    if msg[len(msg) - 1] != "." and msg[len(msg) - 1] != "?":
        await inter.response.send_message(msg.upper() + "!!!")
    else:
        await inter.response.send_message(msg.upper().replace(".", "!!!").replace("?", "!!!"))


@bot.slash_command(description="Yell at a person")
async def yellat(inter, user: str, msg: str):
    if msg[len(msg) - 1] != "." and msg[len(msg) - 1] != "?":
        await inter.response.send_message(f"{user} {msg.upper()}!!!")
    else:
        await inter.response.send_message(f"{user} {msg.upper().replace('.', '!!!').replace('?', '!!!')}")


@bot.slash_command(description="Bans a specified member with an optional reason")
async def ban(ctx, member: disnake.Member, *, reason="Unspecified reason"):
    if member.id == ctx.author.id:
        await ctx.send("You cannot ban yourself, sorry! :)")
        return
    elif member.top_role >= ctx.author.top_role:
        await ctx.send(f"You can only moderate members below your role")
        return
    else:
        await member.ban(reason=reason)
        await ctx.send(embed=embed(ctx, member, reason, "ban"))


@bot.slash_command(description="Kicks a specified member with an optional reason")
async def kick(ctx, member: disnake.Member, *, reason="Unspecified reason"):
    if member.id == ctx.author.id:
        await ctx.send("You cannot kick yourself, sorry! :)")
        return

    if member.top_role >= ctx.author.top_role:
        await ctx.send(f"You can only moderate members below your role")
        return

    else:
        await member.kick(reason=reason)
        await ctx.send(embed=embed(ctx, member, reason, "kick"))


@bot.slash_command(description="Mutes a specified member with an optional reason with time")
async def mute(ctx, member: disnake.Member, *, reason="Unspecified reason"):
    if member.id == ctx.author.id:
        await ctx.send("You cannot mute yourself, sorry! :)")
        return

    if member.top_role >= ctx.author.top_role:
        await ctx.send(f"You can only moderate members below your role")
        return

    else:
        await ctx.send(embed=embed(ctx, member, reason, "mute"))


@bot.slash_command(description="Timeout a specified member with an optional reason and time")
async def timeout(ctx, member: disnake.Member, *, reason="Unspecified reason", days=0, hours=0, minutes=0, seconds=0):
    if member.id == ctx.author.id:
        await ctx.send("You cannot timeout yourself, sorry! :)")
        return

    if member.top_role >= ctx.author.top_role:
        await ctx.send(f"You can only moderate members below your role")
        return

    else:
        duration = timedelta(days=days, hours=hours,
                             minutes=minutes, seconds=seconds)
        await member.timeout(duration=duration, reason=reason)
        await ctx.send(embed=embed(ctx, member, reason, "timeout"))

bot.run(os.environ["token"])
