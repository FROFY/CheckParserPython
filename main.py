# -*- coding: utf-8 -*-
import asyncio
from random import randint
import time

from aiogram.utils import executor
from Telegram.Bot import dp


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


