import time
import config
import discord
from discord.ext import commands


class EverestPins:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ahorn(self, ctx):
        embed = discord.Embed(title="Ahorn Downloads",
                              url="https://github.com/CelestialCartographers/Ahorn",
                              description=("[install_ahorn.jl](https://raw.githubusercontent.com/CelestialCartographers/Ahorn/master/install_ahorn.jl): Cross-platform (Windows, macOS, and Linux)\n"
                                           "[Ahorn for Windows](https://thoas.feralhosting.com/oddstr13/sharex/file/setup-Ahorn-0.0.2.exe): Windows-only quick installer"))

        embed.set_thumbnail(url="https://github.com/CelestialCartographers/Ahorn/blob/master/docs/logo-256.png?raw=true")

        await ctx.send(embed=embed)

    @commands.command()
    async def wiki(self, ctx):
        await ctx.send(embed=discord.Embed(title="Everest Wiki", url="https://github.com/EverestAPI/Resources/wiki"))

    @commands.command()
    async def modstruct(self, ctx):
        await ctx.send(embed=discord.Embed(title="Modstruct Tutorial", url="https://everestapi.github.io/tutorials/modstruct.html", description="Tutorial on how to package your maps"))

    @commands.command()
    async def codemods(self, ctx):
        await ctx.send(embed=discord.Embed(title="Codemodding Tutorial", url="https://everestapi.github.io/tutorials/firstcodemod.html", description="Tutorial on how to modify the game's code"))

def setup(bot):
    bot.add_cog(EverestPins(bot))
