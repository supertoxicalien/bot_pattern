"""
Запуск бота.
"""
from aiogram import executor

from bot import dp
from handlers import base_handlers


async def on_startup(_):
    print('Online')


base_handlers.register_base_handler(dp)

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=on_startup)
