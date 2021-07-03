"""
Copyright (c) 2020-present Axelancerr

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import re

from discord.ext import commands

from core import colours, emojis
from utilities import context, exceptions


COLON_REGEX = re.compile(r'^(?:(?:(?P<hours>[01]?\d|2[0-3]):)?(?P<minutes>[0-5]?\d):)?(?P<seconds>[0-5]?\d)$')
HUMAN_REGEX = re.compile(r'^(?:(?P<hours>[01]?\d|2[0-3])\s?(h|hour|hours)\s?)?(?:(?P<minutes>[0-5]?\d)\s?(m|min|mins|minutes)\s?)?(?:(?P<seconds>[0-5]?\d)\s?(s|sec|secs|seconds))?$')


class TimeConverter(commands.Converter):

    async def convert(self, ctx: context.Context, argument: str) -> int:

        if (match := COLON_REGEX.match(argument)) or (match := HUMAN_REGEX.match(argument)):

            total = 0

            if hours := match.group('hours'):
                total += int(hours) * 60 * 60
            if minutes := match.group('minutes'):
                total += int(minutes) * 60
            if seconds := match.group('seconds'):
                total += int(seconds)

        else:

            try:
                total = int(argument)
            except ValueError:
                raise exceptions.EmbedError(colour=colours.RED, emoji=emojis.CROSS, description='That time format was not recognized.')

        return total
