import random
import discord
from discord.ext import commands
import math
from helpers.checks import check_if_staff_or_ot
import asyncio

class Meme:
    """
    Meme commands.
    """

    def __init__(self, bot):
        self.bot = bot

    def c_to_f(self, c):
        """this is where we take memes too far"""
        return math.floor(9.0 / 5.0 * c + 32)

    def c_to_k(self, c):
        """this is where we take memes REALLY far"""
        return math.floor(c + 273.15)

    @commands.check(check_if_staff_or_ot)
    @commands.command(hidden=True, name="warm")
    async def warm_member(self, ctx, user: discord.Member):
        """Warms a user :3"""
        celsius = random.randint(15, 100)
        fahrenheit = self.c_to_f(celsius)
        kelvin = self.c_to_k(celsius)
        await ctx.send(f"{user.mention} warmed."
                       f" User is now {celsius}°C "
                       f"({fahrenheit}°F, {kelvin}K).")

    @commands.check(check_if_staff_or_ot)
    @commands.command(hidden=True, name="chill", aliases=["cold"])
    async def chill_member(self, ctx, user: discord.Member):
        """Chills a user >:3"""
        celsius = random.randint(-50, 15)
        fahrenheit = self.c_to_f(celsius)
        kelvin = self.c_to_k(celsius)
        await ctx.send(f"{user.mention} chilled."
                       f" User is now {celsius}°C "
                       f"({fahrenheit}°F, {kelvin}K).")

    @commands.check(check_if_staff_or_ot)
    @commands.command(hidden=True)
    async def bones(self, ctx):
        await ctx.send("https://cdn.discordapp.com/emojis/"
                       "443501365843591169.png?v=1")

    @commands.check(check_if_staff_or_ot)
    @commands.command(hidden=True, name="bam")
    async def bam_member(self, ctx, user: discord.Member):
        """Bams a user owo"""
        await ctx.send(f"{self.bot.escape_message(user)} is ̶n͢ow b̕&̡.̷ 👍̡")

    @commands.check(check_if_staff_or_ot)
    @commands.command(hidden=True)
    async def memebercount(self, ctx):
        """Checks memeber count, as requested by dvdfreitag"""
        await ctx.send("There's like, uhhhhh a bunch")

    @commands.check(check_if_staff_or_ot)
    @commands.command(hidden=True)
    async def justmonika(self, ctx):
        """Take 3 guesses... well, 20."""
        chance = random.randint(0, 19)
        if chance == 0:
            await ctx.send("https://ddlc.moe")
        elif chance <= 8:
            tmp = await ctx.send("Just Monika. Just Monika. Just Monika. Just Monika. Justttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt")
            await asyncio.sleep(3)
            await tmp.edit(content="Just Monika.")
        elif chance <= 10:
            await ctx.send("[SarCATstic is upset.]")
        elif chance <= 12:
            await ctx.send("[0x0ade is upset.]")
        elif chance <= 18:
            tmp = await ctx.send("You can't make me.")
            await asyncio.sleep(10)
            await tmp.edit(content="🅸 🅲🅷🅰🅽🅶🅴🅳 🅼🆈 🅼🅸🅽🅳. 🅹🆄🆂🆃 🅼🅾🅽🅸🅺🅰")
        else:
            await ctx.send("<a:monikadefaultdance:529075909651726346>")

def setup(bot):
    bot.add_cog(Meme(bot))
