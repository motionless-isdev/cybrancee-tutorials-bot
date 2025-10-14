import discord
from discord.ext import commands

class Hi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="hola", description="Hola como estas!")
    async def hola(self, ctx):
        """Holaaaaaaa"""
        await ctx.send("Hola! 👋")

async def setup(bot):
    await bot.add_cog(Hi(bot))
