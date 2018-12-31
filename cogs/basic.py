import time
import config
import discord
from discord.ext import commands


class Basic:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        """Says hello. Duh."""
        await ctx.send(f"Hello {ctx.author.mention}!")

    #@commands.command()
    #async def modrules(self, ctx, *, targetuser: discord.Member = None):
    #    """Post a link to the Rules"""
    #    if not targetuser:
    #        targetuser = ctx.author
    #    await ctx.send(f"{targetuser.mention}: The rules for the modding section "
    #                   f"can be found here: #modding_welcome")

    #@commands.command()
    #async def rules(self, ctx, *, targetuser: discord.Member = None):
    #    """Post a link to the Rules"""
    #    if not targetuser:
    #        targetuser = ctx.author
    #    await ctx.send(f"{targetuser.mention}: The rules for the server "
    #                   f"can be found here: #welcome")

    @commands.guild_only()
    @commands.command()
    async def membercount(self, ctx):
        """Prints the member count of the server."""
        await ctx.send(f"{ctx.guild.name} has "
                       f"{ctx.guild.member_count} members!")

    @commands.command()
    async def source(self, ctx):
        """Gives link to source code."""
        await ctx.send("You can find my source at " +
                       config.source_url +
                       ".")

    @commands.command(aliases=["robocopng", "robocop-ng", "everestbot"])
    async def robocop(self, ctx):
        """Shows a quick embed with bot info."""
        embed = discord.Embed(title="Robocop-NG",
                              url=config.source_url,
                              description=config.embed_desc)

        embed.set_thumbnail(url=self.bot.user.avatar_url)

        await ctx.send(embed=embed)

    @commands.command(aliases=['p'])
    async def ping(self, ctx):
        """Shows ping values to discord.

        RTT = Round-trip time, time taken to send a message to discord
        GW = Gateway Ping"""
        before = time.monotonic()
        tmp = await ctx.send('Calculating ping...')
        after = time.monotonic()
        rtt_ms = (after - before) * 1000
        gw_ms = self.bot.latency * 1000

        message_text = f":ping_pong: rtt: `{rtt_ms:.1f}ms`, `gw: {gw_ms:.1f}ms`"
        self.bot.log.info(message_text)
        await tmp.edit(content=message_text)


def setup(bot):
    bot.add_cog(Basic(bot))
