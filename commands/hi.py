import discord
from discord.ext import commands

class Hi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="hi", description="Say hi to the bot")
    async def hi(self, ctx):
        """This command works for both !hi and /hi"""
        await ctx.send("Hi there! 👋")

async def setup(bot):
    await bot.add_cog(Hi(bot))
