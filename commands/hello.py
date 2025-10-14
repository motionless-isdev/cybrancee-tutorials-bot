import discord
from discord.ext import commands

class Hi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="hello", description="Say hello to the bot")
    async def hello(self, ctx):
        """This command works for both !hello and /hello"""
        await ctx.send("Hello there! 👋")

async def setup(bot):
    await bot.add_cog(Hi(bot))
