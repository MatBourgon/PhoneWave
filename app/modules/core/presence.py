from discord.ext import commands

from app.utilities import logger


class Presence(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info(f"Logged in as {self.bot.user.name}")

    @commands.Cog.listener()
    async def on_error(self, event, *args, **kwargs):
        logger.error(f"Error in {event}", exc_info=True)

    @commands.command()
    async def test(self, ctx: commands.Context):
        await ctx.send("test")


def setup(bot):
    bot.add_cog(Presence(bot))
