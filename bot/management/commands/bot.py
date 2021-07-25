import asyncio

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from django.core.management import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    help = 'Бот, для уведомлений'

    def handle(self, *args, **options):
        executor.start_polling(dp)


storage = MemoryStorage()
bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot, storage=storage)
chat_id = settings.TELEGRAM_CHAT_ID


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
	return await message.reply('okey')