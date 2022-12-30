import disnake
from disnake.ext import commands
import json
import random

hint = 0

class HighLow(disnake.ui.View):
    def __init__(self, hint):
        super().__init__(timeout=None)
        self.num = random.randint(1, 100)
        self.hint = hint

    @disnake.ui.button(label="Lower", style=disnake.ButtonStyle.green, custom_id="highlow:lower")
    async def lower(self, button: disnake.ui.Button, ctx: disnake.MessageInteraction):
        if self.num < self.hint:
            gains = random.randint(250, 1000)
            await ctx.send(f"Congrats! You won :popcorn:{gains}!")
            with open("popcorn.json", "r+") as file:
                with open("popcorn.json", "w") as file2:
                    try:
                        popcorn = json.loads(file.read())
                    except:
                        popcorn = {}
                    try:
                        popcorn[ctx.author.name + "#" + ctx.author.discriminator]["popcornAmount"] += gains
                    except:
                        popcorn[ctx.author.name + "#" + ctx.author.discriminator] = {}
                        popcorn[ctx.author.name + "#" + ctx.author.discriminator]["popcornAmount"] = gains
                    file2.write(json.dumps(popcorn))
        else:
            await ctx.send(f"You lost! The number was {self.num}. Your hint was {self.hint}")

    @disnake.ui.button(label="JACKPOT!!!", style=disnake.ButtonStyle.grey, custom_id="highlow:jackpot")
    async def jackpot(self, button: disnake.ui.Button, ctx: disnake.MessageInteraction):
        if self.num == self.hint:
            gains = random.randint(250, 1000)
            await ctx.send(f"Congrats! You won :popcorn:{gains}!")
            with open("popcorn.json", "r+") as file:
                with open("popcorn.json", "w") as file2:
                    try:
                        popcorn = json.loads(file.read())
                    except:
                        popcorn = {}
                    try:
                        popcorn[ctx.author.name + "#" + ctx.author.discriminator]["popcornAmount"] += gains
                    except:
                        popcorn[ctx.author.name + "#" + ctx.author.discriminator] = {}
                        popcorn[ctx.author.name + "#" + ctx.author.discriminator]["popcornAmount"] = gains
                    file2.write(json.dumps(popcorn))
        else:
            await ctx.send(f"You lost! The number was {self.num}. Your hint was {self.hint}")
    
    @disnake.ui.button(label="Higher", style=disnake.ButtonStyle.red, custom_id="highlow:higher")
    async def higher(self, button: disnake.ui.Button, ctx: disnake.MessageInteraction):
        if self.num > self.hint:
            gains = random.randint(250, 1000)
            await ctx.send(f"Congrats! You won :popcorn:{gains}!")
            with open("popcorn.json", "r+") as file:
                with open("popcorn.json", "w") as file2:
                    try:
                        popcorn = json.loads(file.read())
                    except:
                        popcorn = {}
                    try:
                        popcorn[ctx.author.name + "#" + ctx.author.discriminator]["popcornAmount"] += gains
                    except:
                        popcorn[ctx.author.name + "#" + ctx.author.discriminator] = {}
                        popcorn[ctx.author.name + "#" + ctx.author.discriminator]["popcornAmount"] = gains
                    file2.write(json.dumps(popcorn))
        else:
            await ctx.send(f"You lost! The number was {self.num}. Your hint was {self.hint}")



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

    @commands.slash_command(description="Get a chance of winning a lot of popcorn by guessing my number")
    async def highlow(self, ctx):
        hint = random.randint(1, 100)
        embed = disnake.Embed(
            title="Highlow",
            description=f"Guess my number and I'll give you some popcorn :popcorn:. Your hint is {hint}"
        )
        await ctx.send(embed=embed, view=HighLow(hint))

def setup(bot):
    bot.add_cog(PopcornCommands(bot))
