# -*- coding: utf-8 -*-
import asyncio
from random import randint
import time

from aiogram.utils import executor
from Telegram.Bot import dp


def is_even(num):
    if num in [1, 3, 5, 7, 9]:
        return False
    if num == 2:
        return True
    while True:
        a, b = randint(0, num), randint(0, num)
        print(time.time() - start_time)

        if (a * b) == num:
            return is_even(a) or is_even(b)


if __name__ == '__main__':
    #executor.start_polling(dp, skip_updates=True)
    # orders = GetOrder.OrderWithStr('t=20221102T1352&s=89.99&fn=9960440301834413&i=6073&fp=1929603051&n=1')
    # print(f'Название: {orders[0]}\nКоличество: {orders[2]}\nЦена: {orders[1]}р')
    start_time = time.time()
    print(is_even(10001))
    print(time.time() - start_time)


