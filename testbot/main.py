import asyncio
from aiogram import Bot, Dispatcher, executor
loop = asyncio.new_event_loop()
bot = Bot(token='5642318179:AAHRSLNE7A0fkHYduS_XiRsSQ4EFh2U-A6w', parse_mode='HTML')
dp = Dispatcher(bot, loop)

if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp)
