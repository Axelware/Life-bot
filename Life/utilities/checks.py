from discord.ext import commands


def is_player_connected():
    async def predicate(ctx):
        if not ctx.player.is_connected:
            raise commands.CheckFailure(f"I am not connected to any voice channels.")
        return True
    return commands.check(predicate)


def is_player_playing():
    async def predicate(ctx):
        if not ctx.player.is_playing:
            raise commands.CheckFailure(f"I am not currently playing anything.")
        return True
    return commands.check(predicate)


def is_member_connected():
    async def predicate(ctx):
        if not ctx.author.voice:
            raise commands.CheckFailure(f"You are not connected to any voice channels.")
        return True
    return commands.check(predicate)


def is_member_in_channel():
    async def predicate(ctx):
        if not ctx.player.voice_channel.id == ctx.author.voice.channel.id:
            raise commands.CheckFailure(f"You are not connected to the same voice channel as me.")
        return True
    return commands.check(predicate)
