import asyncio
import os
import aiohttp
from handlers import router
from aiogram import Bot,Dispatcher
from dotenv import load_dotenv
async def main():
    dp = Dispatcher()
    load_dotenv()
    bot = Bot(token = os.getenv('TOKEN'))
    dp.include_router(router)
    await dp.start_polling(bot)
if __name__ == '__main__':
    try:
        print('бот запущен')
        asyncio.run(main())
    except aiohttp.ClientError as e:
        print(f'ошибка подключения: {e}')
    except KeyboardInterrupt:
        print('бот выключен')
        
        


