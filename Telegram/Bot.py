import io

from aiogram import Bot, Dispatcher, executor, types
import asyncio
import logging
import psycopg2
import uuid

import QRParse.QrAPI
from DBFunc.DBMethods import *
import config


from QRParse.GetOrder import OrderWithStr
from QRParse.QrAPI import get_order_photo
from Telegram.Keyboard import keyboard

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.tg_token)

dp = Dispatcher(bot)


# @dp.message_handler()
# async def echo(message: types.Message):
#     answer = f'Уважаю тебя {message.from_user.username}'
#     await message.answer(answer)
#     print(f'От: {message.from_user.username} | Сообщение: {message.text} | Ответ: {answer}')


@dp.message_handler(lambda message: message.text == "Получить из базы")
async def orders(message: types.Message):
    records = db_data()
    await message.answer(f'{records}')


@dp.message_handler(commands=['orders'])
async def orders(message: types.Message):
    orders = OrderWithStr('t=20221102T1352&s=89.99&fn=9960440301834413&i=6073&fp=1929603051&n=1')
    await message.answer(f'Название: {orders[0]}\nКоличество: {orders[2]}\nЦена: {orders[1]}р')


@dp.message_handler(content_types=['photo'])
async def get_photo(message: types.Message):
    unique_name = uuid.uuid4()
    await message.photo[-1].download(
        destination_file=f'tmp//{unique_name}.png')
    data = QRParse.QrAPI.get_order_photo(f'tmp//{unique_name}.png')
    items, price = QRParse.GetOrder.parse_json(data)
    for i in range(len(items)):
        await message.answer(f'Товар: {items[i]}\nЦена: {price[i]}р')


@dp.message_handler(commands=['qrcode'])
async def orders(message: types.Message):
    orders = OrderWithPhoto()
    await message.answer(orders["data"]["json"]["items"][0]["name"])


@dp.message_handler(commands=['start'])
async def start_fn(message: types.Message):
    await message.answer(f'Приветствую {message.from_user.username}', reply_markup=keyboard)@dp.message_handler(commands=['start'])


@dp.message_handler(commands=['insert'])
async def start_fn(message: types.Message):
    db_insert(1)
    await message.answer('Выполняю', reply_markup=keyboard)
