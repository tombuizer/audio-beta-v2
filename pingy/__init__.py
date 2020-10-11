  
from .pingy import Pingy


def setup(bot):
    bot.add_cog(Pingy(bot))
