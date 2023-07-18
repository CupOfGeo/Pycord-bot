import aiohttp
import asyncio
import discord
from discord.ext import commands

from helpers import checks


class Me(commands.Cog, name="me"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()  # Create a slash command for the supplied guilds.
    async def hellome(self, ctx: discord.ApplicationContext):
        await ctx.send("Hi, this is a slash command from a cog!")

    @commands.command(name="joinme", description="join VC")
    async def join(self, ctx: discord.ApplicationContext):
        channel = ctx.message.author.voice.channel
        if not channel:
            await ctx.send("You are not connected to a voice channel")
            return
        voice_channel = await channel.connect()
        
        await asyncio.sleep(1)
        if not discord.opus.is_loaded():
            discord.opus.load_opus("/home/linuxbrew/.linuxbrew/lib/libopus.so.0") 
        # Start playing the audio file
        ctx.voice_client.play(discord.FFmpegPCMAudio(executable="ffmpeg", source="/workspaces/Python-Discord-Bot-Template/Hello.mp3"))
        

        

    @commands.command(name="dummy", description="Get dummy")
    @checks.not_blacklisted()
    async def randomfact(self, context: discord.ApplicationContext) -> None:
        """
        Get a dummy

        :param context: The hybrid command context.
        """
        # This will prevent your bot from stopping everything when doing a web request - see: https://discordpy.readthedocs.io/en/stable/faq.html#how-do-i-make-a-web-request
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://georges-playground.com/api/dummy/?limit=10&offset=0"
            ) as request:
                if request.status == 200:
                    data = await request.json()
                    embed = discord.Embed(description=data["text"], color=0xD75BF4)
                else:
                    embed = discord.Embed(
                        title="Error!",
                        description="There is something wrong with the API, please try again later",
                        color=0xE02B2B,
                    )
                await context.send(embed=embed)


def setup(bot):
    bot.add_cog(Me(bot))