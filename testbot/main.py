import asyncio
from aiogram import Bot, Dispatcher, executor
loop = asyncio.new_event_loop()
bot = Bot(token='5813307847:AAHtB8yiu3NXC88CjKeql03g83TZu81pim8', parse_mode='HTML')
dp = Dispatcher(bot, loop)

if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp)
