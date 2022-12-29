import disnake
from disnake.ext import commands
import json
import random


class PopcornCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.places = [{
            "name": "dog",
            "chance": 5,
            "amountMax": 15,
            "amountMin": 1
        }, {
            "name": "pantry",
            "chance": 2,
            "amountMax": 300,
            "amountMin": 150
        }, {
            "name": "wallet",
            "chance": 5,
            "amountMax": 3,
            "amountMin": 1
        }, {
            "name": "movie theatre",
            "chance": 1,
            "amountMax": 500,
            "amountMin": 350
        }, {
            "name": "roommate",
            "chance": 3,
            "amountMax": 150,
            "amountMin": 75
        }]

    @commands.slash_command(description="Checks your popcorn status")
    async def popcornstatus(self, ctx):
        with open("popcorn.json", "r+") as file:
            try:
                popcornStuff = json.loads(file.read())
            except:
                popcornStuff = {}
            member = ctx.author
            data = 0
            try:
                data = popcornStuff[member.name + "#" +
                                     member.discriminator]["popcornAmount"]
            except:
                popcornStuff[member.name + "#" +
                                     member.discriminator] = {}
                popcornStuff[member.name + "#" + member.discriminator]["popcornAmount"] = 0
                data = popcornStuff[member.name + "#" +
                                     member.discriminator]["popcornAmount"]
                jsonString = json.dumps(popcornStuff)
                file.write(jsonString)
            finally:
                embed = disnake.Embed(
                    title="Popcorn Status",
                    description=f"The amount popcorn {member.name + '#' + member.discriminator} has is {data}"
                )
                await ctx.send(embed=embed)

    @commands.slash_command(description="Search for Popcorn")
    async def searchforpopcorn(self, ctx):
        with open("popcorn.json", "r+") as file:
            try:
                popcornStuff = json.loads(file.read())
            except:
                popcornStuff = {}
            place = random.choice(self.places)
            gains = 0
            title = f"You searched the {place['name']}"
            description = f""
            member = ctx.author

            if random.randint(1, place["chance"]) == 1:
                gains = random.randint(place["amountMin"], place["amountMax"])
            if gains == 0:
                description = f"LMFAO!!!! You searched the {place['name']} and found not a single piece of popcorn! Imagine not finding a single piece of popcorn. Like, couldn't be me!"
            else:
                description = f"Congrats! You found {gains} pieces of popcorn in the {place['name']}"

            try:
                popcornStuff[member.name + "#" +
                                     member.discriminator]["popcornAmount"] += gains
            except:
                popcornStuff[member.name + "#" +
                                     member.discriminator] = {}
                popcornStuff[member.name + "#" + member.discriminator]["popcornAmount"] = gains
            
            embed = disnake.Embed(
                title=title,
                description=description
            )

            await ctx.send(embed=embed)
    
    @commands.slash_command(description="Guess the number")
    async def highlow(self, inter: disnake.ApplicationCommandInteraction):
        num = random.randint(1, 100)
        hint = random.randint(1, 100)
        await inter.response.send_message(
            f"Guess my number\n\nYour hint is {hint}\n\nPress high if you think it is higher than the hint, lower if you think it's lower, and JACKPOT! if you think it is the hint",
            components=[
                disnake.ui.Button(label="Lower", style=disnake.ButtonStyle.blurple, custom_id="lower"),
                disnake.ui.Button(label="JACKPOT!", style=disnake.ButtonStyle.grey, custom_id="jackpot"),
                disnake.ui.Button(label="Higher", style=disnake.ButtonStyle.blurple, custom_id="higher")
            ]
        )

def setup(bot):
    bot.add_cog(PopcornCommands(bot))
