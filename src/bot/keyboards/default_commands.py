from __future__ import annotations
from typing import TYPE_CHECKING

from aiogram.types import BotCommand, BotCommandScopeDefault

if TYPE_CHECKING:
    from aiogram import Bot

users_commands = {
    "menu": "main menu",
    "info": "information about company",
    "support": "support",
    # "help": "help",
}


async def set_default_commands(bot: Bot) -> None:
    await remove_default_commands(bot)

    for command, description in users_commands.items():
        await bot.set_my_commands(
            [BotCommand(command=command, description=description)], scope=BotCommandScopeDefault()
        )


async def remove_default_commands(bot: Bot) -> None:
    await bot.delete_my_commands(scope=BotCommandScopeDefault())
