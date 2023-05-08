"""
Обработка базовых заголовков.
"""

from aiogram import types, Dispatcher

from settings.settings import HELP_TEXT


async def start_command(msg: types.Message) -> None:
    await msg.answer("Добро пожаловать!")


async def help_command(msg: types.Message) -> None:
    await msg.answer(HELP_TEXT)


def register_base_handler(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(help_command, commands=['help'])