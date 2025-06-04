# backend/users/telegram/handlers.py
from aiogram import F, Router
from aiogram.types import Message

router = Router()

@router.message(F.text == "/start")
async def handle_start(message: Message):
    await message.answer(
        "Привет! Введи команду <code>/verify 123456</code>, чтобы подтвердиться.",
        parse_mode="HTML"
    )

@router.message(F.text.startswith("/verify "))
async def handle_verify(message: Message):
    code = message.text.split("/verify ", 1)[1].strip()
    await message.answer(f"Ты ввёл код: <code>{code}</code>", parse_mode="HTML")
