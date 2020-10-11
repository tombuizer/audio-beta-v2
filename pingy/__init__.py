  
from .pingy import pingy


def setup(bot):
    bot.add_cog(pingy(bot))
