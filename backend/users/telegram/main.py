# backend/users/telegram/main.py
import asyncio
from backend.users.telegram.bot import bot, dp
from backend.users.telegram.handlers import router

async def main():
    print(">>> main() запущена")
    dp.include_router(router)  # <-- подключаем router
    await dp.start_polling(bot)

def run():
    print(">>> run() запущена")
    asyncio.run(main())

run()
