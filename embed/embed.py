let Embed = new Discord.MessageEmbed()
    .setTitle()
    .setAuthor()
    .setColor()
    .addField()
    .setDescription()
    .setThumbnail()

from redbot.core import commands

class Embed(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def putin(self, ctx):
        """This does stuff!"""
        {
  "embeds": [
    {
      "title": "info",
      "description": "Putin is an multifunction discord bot created to make your server easier to run and more fun.",
      "fields": [
        {
          "name": "Discord.py",
          "value": "[1.4.1](https://pypi.org/project/discord.py/)",
          "inline": true
        },
        {
          "name": "Python",
          "value": "[3.8.5](https://www.python.org/)",
          "inline": true
        }
      ],
      "author": {
        "name": "Cyktom#3882",
        "icon_url": "https://cdn.discordapp.com/avatars/298190347614552066/a_d6411b8e369a7757b137fe84edbd4416.gif?size=1024"
      },
      "footer": {
        "text": "putin bot 2020"
      }
    }
  ]
}