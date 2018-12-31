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
                              description=("• [install_ahorn.jl](https://raw.githubusercontent.com/CelestialCartographers/Ahorn/master/install_ahorn.jl): Cross-platform (Windows, macOS, and Linux)\n"
                                           "• [Ahorn for Windows](https://thoas.feralhosting.com/oddstr13/sharex/file/setup-Ahorn-0.0.2.exe): Windows-only quick installer"))

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

    @commands.command()
    async def piracy(self, ctx):
        await ctx.send("Everest does not support pirated copies of the game. These are banned on the server, and are often too outdated for many maps. Please purchase the game legitimately.")

    @commands.command()
    async def tutorials(self, ctx):
        embed = discord.Embed(title="Tutorial List",
                              description=("• [How do I package my maps?](https://everestapi.github.io/tutorials/modstruct.html)\n"
                                           "• [How do I modify the game's code?](https://everestapi.github.io/tutorials/firstcodemod.html)\n"
                                           "• [How do I install mods on PC?](https://github.com/EverestAPI/Resources/wiki/How-do-I-install-mods-on-PC%3F)\n"
                                           "• [How do I make maps on PC?](https://github.com/EverestAPI/Resources/wiki/How-do-I-make-maps-on-PC%3F)\n"
                                           "• [How do I play Celeste with others over the internet? (GhostNet)](https://github.com/EverestAPI/Resources/wiki/How-do-I-play-Celeste-with-others-over-the-internet%3F-%28GhostNet%29)\n"
                                           "• [What's going on with mods on Nintendo Switch?](https://github.com/EverestAPI/Resources/wiki/What%27s-going-on-with-mods-on-Nintendo-Switch%3F)"))

        embed.set_thumbnail(url="https://everestapi.github.io/logo.png")

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(EverestPins(bot))
