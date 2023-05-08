"""
Настройка проекта:
Работа с переменными окружения.
"""
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

HELP_TEXT = '''
Основные команды бота:
/start -> Запуск бота.
/help -> Список команд.
'''