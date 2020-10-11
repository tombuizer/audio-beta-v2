from redbot.core import commands

class Mycog(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def brr(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("<@738981683516145785>")