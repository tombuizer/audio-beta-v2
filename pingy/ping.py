from discord.ext import menus, commands
import discord
import time
import aiohttp
import html2text
from redbot.core import Config, commands
from redbot.core.bot import Red
from redbot.core.commands import Cog
from redbot.core.utils.chat_formatting import pagify

class PingRepeat(menus.Menu):
    
    def __init__(self,bot:commands.Bot, p: int, original_ctx: commands.Context):
        super().__init__(timeout=30.0,clear_reactions_after=True)
        self.p = p
        self.bot = bot
        self.original_ctx = original_ctx
        self.pingindex = 1
        
    async def send_initial_message(self, ctx, channel):
        t_start = time.time()
        m = await ctx.channel.send("Testing RTT for message editing.")
        send = time.time() - t_start
        await m.edit(content="Testing Message Edit: Run 1...")
        rtt1 = time.time() - t_start - send
        await m.edit(content="Testing Message Edit: Run 2...")
        rtt2 = time.time() - t_start - (rtt1 + send)
        await m.edit(content="Testing Message Edit: Run 3...")
        rtt3 = time.time() - t_start - (rtt1 + rtt2 + send)
        avg = (rtt1 + rtt2 + rtt3) / 3
        minimum = min(rtt1, rtt2, rtt3)*1000
        maximum = max(rtt1, rtt2, rtt3)*1000
        ds = time.time()
        await m.delete()
        delete = time.time() - ds
        
        embed = discord.Embed(title="StatBot Ping", description=f"Websocket latency: {round(self.bot.latency*1000, self.p)}ms", colour=0xF81894)
        embed.add_field(name="Message Send", value=f"{round(send*1000, self.p)}ms")
        embed.add_field(name="Message Delete", value=f"{round(delete*1000, self.p)}ms")
        embed.add_field(name="Edit RTT Average/Minimum/Maximum/Difference", value=f"{round(avg*1000, self.p)}ms / {round(minimum, self.p)}ms / {round(maximum, self.p)}ms / {round(maximum - minimum, self.p)}ms", inline=False)
        embed.add_field(name="Edit RTT Run 1", value=f"{round(rtt1*1000, self.p)}ms")
        embed.add_field(name="Edit RTT Run 2", value=f"{round(rtt2*1000, self.p)}ms")
        embed.add_field(name="Edit RTT Run 3", value=f"{round(rtt3*1000, self.p)}ms")
        embed.set_footer(text="Replicated from vcokltfre#6868's ResearchBot for Minecraft@Home.")
        
        return await channel.send(embed=embed)
    
    @menus.button('🔁')
    async def repeat_again(self,payload: discord.RawReactionActionEvent):
        if payload.event_type == "REACTION_REMOVE" or payload.user_id not in [self.original_ctx.author.id, self.bot.owner_id]:
            return
        t_start = time.time()
        self.message: discord.Message
        m = await self.bot.get_channel(payload.channel_id).send("Testing RTT for message editing.")
        await self.message.remove_reaction('🔁',self.bot.get_guild(payload.guild_id).get_member(payload.user_id))
        send = time.time() - t_start
        await m.edit(content="Testing Message Edit: Run 1...")
        rtt1 = time.time() - t_start - send
        await m.edit(content="Testing Message Edit: Run 2...")
        rtt2 = time.time() - t_start - (rtt1 + send)
        await m.edit(content="Testing Message Edit: Run 3...")
        rtt3 = time.time() - t_start - (rtt1 + rtt2 + send)
        avg = (rtt1 + rtt2 + rtt3) / 3
        minimum = min(rtt1, rtt2, rtt3)*1000
        maximum = max(rtt1, rtt2, rtt3)*1000
        ds = time.time()
        await m.delete()
        delete = time.time() - ds
        self.pingindex += 1 
        embed = discord.Embed(title=f"StatBot Ping - {self.pingindex}", description=f"Websocket latency: {round(self.bot.latency*1000, self.p)}ms", colour=0xF81894)
        embed.add_field(name="Message Send", value=f"{round(send*1000, self.p)}ms")
        embed.add_field(name="Message Delete", value=f"{round(delete*1000, self.p)}ms")
        embed.add_field(name="Edit RTT Average/Minimum/Maximum/Difference", value=f"{round(avg*1000, self.p)}ms / {round(minimum, self.p)}ms / {round(maximum, self.p)}ms / {round(maximum - minimum, self.p)}ms", inline=False)
        embed.add_field(name="Edit RTT Run 1", value=f"{round(rtt1*1000, self.p)}ms")
        embed.add_field(name="Edit RTT Run 2", value=f"{round(rtt2*1000, self.p)}ms")
        embed.add_field(name="Edit RTT Run 3", value=f"{round(rtt3*1000, self.p)}ms")
        embed.set_footer(text="Replicated from vcokltfre#6868's ResearchBot for Minecraft@Home.")
        
        await self.message.edit(embed=embed)

    @menus.button('\N{BLACK SQUARE FOR STOP}\ufe0f')
    async def on_stop(self, payload):
        if payload.user_id not in [self.original_ctx.author.id, self.bot.owner_id]:
            return
        self.stop()