from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.middlewares import BaseMiddleware
import sqlite_db
import asyncio
import os
import datetime
import create_excel


def get_start_kb() -> ReplyKeyboardMarkup:
	kb = ReplyKeyboardMarkup(keyboard=[
		[KeyboardButton('/get_today_statistic')]

	], resize_keyboard=True)
	return kb


storage = MemoryStorage()
bot = Bot("")
dp = Dispatcher(bot, storage=storage)
now = datetime.datetime.today().strftime('%Y-%m-%d')

@dp.message_handler(commands=['get_today_statistic'], state='*')
async def cmd_cancel(message: types.Message) -> None:
	await bot.send_message(chat_id=message.from_user.id, text='Доброго дня! Статистика за добу:', reply_markup=get_start_kb())
	sqlite_db.db_connect()
	create_excel.create_statistic_file()

	await bot.send_document(message.from_user.id, open('report.xlsx', 'rb'))
	
if __name__ == '__main__':
	dp.middleware.setup(BaseMiddleware())
	executor.start_polling(dispatcher=dp, skip_updates=True)

