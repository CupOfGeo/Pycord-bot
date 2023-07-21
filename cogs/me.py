import asyncio
import discord
from discord.ext import commands
import io
import pydub  # pip install pydub==0.25.1
from discord.sinks import MP3Sink
import copy
# from helpers import checks


async def finished_callback(sink: MP3Sink, channel: discord.TextChannel):
    mention_strs = []
    audio_segments: list[pydub.AudioSegment] = []
    files: list[discord.File] = []

    longest = pydub.AudioSegment.empty()

    # each user has its own audio file but we merge them all together 
    for user_id, audio in sink.audio_data.items():
        mention_strs.append(f"<@{user_id}>")

        seg = pydub.AudioSegment.from_file(audio.file, format="mp3")

        # Determine the longest audio segment
        if len(seg) > len(longest):
            audio_segments.append(longest)
            longest = seg
        else:
            audio_segments.append(seg)

        audio.file.seek(0)
        files.append(discord.File(audio.file, filename=f"{user_id}.mp3"))

    for seg in audio_segments:
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
        # self.sink = MP3Sink()
        self.send_audio_task = None

    async def send_audio_to_channel(self, channel: discord.TextChannel, vc):
        while True:
            await asyncio.sleep(3)  # Adjust the interval as needed
            await channel.send("3 secs")
            vc.stop_recording()
            await channel.send("sending to whisper")  # doesn't work without this?
            vc.start_recording(MP3Sink(), finished_callback, channel)

    @commands.command()
    async def join(self, ctx: discord.ApplicationContext):
        """Join the voice channel!"""
        voice = ctx.author.voice

        if not voice:
            return await ctx.send("You're not in a vc right now")

        await voice.channel.connect()
        await asyncio.sleep(1)
        # Start playing the audio file
        ctx.voice_client.play(discord.FFmpegPCMAudio(executable="ffmpeg", source="Hello.mp3"))

        await ctx.send("Joined!")

    @commands.command()
    async def start(self, ctx: discord.ApplicationContext):
        await self.join(ctx)
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

        if self.send_audio_task is None:
            self.send_audio_task = asyncio.create_task(
                self.send_audio_to_channel(ctx.channel, vc)
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
