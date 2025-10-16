import discord
from discord.ext import commands

class Hi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="sayhi", description="Another Hi")
    async def sayhi(self, ctx):
        """HIIIIIII"""
        await ctx.send("Hiiiiii!")

        # Hello this is a change

async def setup(bot):
    await bot.add_cog(Hi(bot))
