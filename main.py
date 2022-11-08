# -*- coding: utf-8 -*-
import asyncio

from aiogram.utils import executor
from Telegram.Bot import dp

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    # orders = GetOrder.OrderWithStr('t=20221102T1352&s=89.99&fn=9960440301834413&i=6073&fp=1929603051&n=1')
    # print(f'Название: {orders[0]}\nКоличество: {orders[2]}\nЦена: {orders[1]}р')
