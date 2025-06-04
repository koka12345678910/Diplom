# backend/users/telegram/bot.py
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

BOT_TOKEN = '7892554463:AAFcX6vj_Vzo_B2PtY4Yza_By0zjILRVTR8'

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()
