import aiohttp
import asyncio
import discord
from discord.ext import commands
import io
import pydub  # pip install pydub==0.25.1
from discord.sinks import MP3Sink

from helpers import checks


async def finished_callback(sink: MP3Sink, channel: discord.TextChannel):
    mention_strs = []
    audio_segs: list[pydub.AudioSegment] = []
    files: list[discord.File] = []

    longest = pydub.AudioSegment.empty()

    for user_id, audio in sink.audio_data.items():
        mention_strs.append(f"<@{user_id}>")

        seg = pydub.AudioSegment.from_file(audio.file, format="mp3")

        # Determine the longest audio segment
        if len(seg) > len(longest):
            audio_segs.append(longest)
            longest = seg
        else:
            audio_segs.append(seg)

        audio.file.seek(0)
        files.append(discord.File(audio.file, filename=f"{user_id}.mp3"))

    for seg in audio_segs:
        longest = longest.overlay(seg)

    with io.BytesIO() as f:
        longest.export(f, format="mp3")
        await channel.send(
            f"Finished! Recorded audio for {', '.join(mention_strs)}.",
            files=files + [discord.File(f, filename="recording.mp3")],
        )


class Me(commands.Cog, name="me"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()  # Create a slash command for the supplied guilds.
    async def hellome(self, ctx: discord.ApplicationContext):
        await ctx.send("Hi, this is a slash command from a cog!")

    @commands.command(name="joinme", description="join VC")
    async def hello(self, ctx: discord.ApplicationContext):
        channel = ctx.message.author.voice.channel
        if not channel:
            await ctx.send("You are not connected to a voice channel")
            return
        # voice_channel =
        await channel.connect()
        await asyncio.sleep(1)
        # Start playing the audio file
        ctx.voice_client.play(discord.FFmpegPCMAudio(executable="ffmpeg", source="Hello.mp3"))
        return
  
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

    @commands.command()
    async def join(self, ctx: discord.ApplicationContext):
        """Join the voice channel!"""
        voice = ctx.author.voice

        if not voice:
            return await ctx.send("You're not in a vc right now")

        await voice.channel.connect()

        await ctx.send("Joined!")

    @commands.command()
    async def start(self, ctx: discord.ApplicationContext):
        """Record the voice channel!"""
        voice = ctx.author.voice

        if not voice:
            return await ctx.send("You're not in a vc right now")

        vc: discord.VoiceClient = ctx.voice_client

        if not vc:
            return await ctx.send(
                "I'm not in a vc right now. Use `/join` to make me join!"
            )

        vc.start_recording(
            MP3Sink(),
            finished_callback,
            ctx.channel,
            # sync_start=True,  # WARNING: This feature is very unstable and may break at any time.
        )

        await ctx.send("The recording has started!")

    @commands.command()
    async def stop(self, ctx: discord.ApplicationContext):
        """Stop the recording"""
        vc: discord.VoiceClient = ctx.voice_client

        if not vc:
            return await ctx.send("There's no recording going on right now")

        vc.stop_recording()

        await ctx.send("The recording has stopped!")

    @commands.command()
    async def leave(self, ctx: discord.ApplicationContext):
        """Leave the voice channel!"""
        vc: discord.VoiceClient = ctx.voice_client

        if not vc:
            return await ctx.send("I'm not in a vc right now")

        await vc.disconnect()

        await ctx.send("Left!")


def setup(bot):
    bot.add_cog(Me(bot))
