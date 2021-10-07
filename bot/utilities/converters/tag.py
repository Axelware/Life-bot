# Future
from __future__ import annotations

# Standard Library
from typing import Any

# Packages
from discord.ext import commands

# My stuff
from core import colours, emojis
from utilities import custom, exceptions


class TagNameConverter(commands.clean_content):

    async def convert(self, ctx: custom.Context, argument: str) -> str:

        self.escape_markdown = True

        if not (argument := (await super().convert(ctx=ctx, argument=argument)).strip()):
            raise commands.BadArgument

        command: Any = ctx.bot.get_command("tag")

        if argument.split(" ")[0] in (names := command.all_commands.keys()):
            raise exceptions.EmbedError(
                colour=colours.RED,
                emoji=emojis.CROSS,
                description=f"Tag names can not start with a tag subcommand name. ({', '.join(f'`{name}`' for name in names)})",
            )
        if len(argument) < 3 or len(argument) > 50:
            raise exceptions.EmbedError(
                colour=colours.RED,
                emoji=emojis.CROSS,
                description="Tag names must be between 3 and 50 characters long."
            )

        return argument


class TagContentConverter(commands.clean_content):

    async def convert(self, ctx: custom.Context, argument: str) -> str:

        if not (argument := (await super().convert(ctx=ctx, argument=argument)).strip()):
            raise commands.BadArgument

        if len(argument) > 1500:
            raise exceptions.EmbedError(
                colour=colours.RED,
                emoji=emojis.CROSS,
                description="Tag content can not be more than 1500 characters long."
            )

        return argument
