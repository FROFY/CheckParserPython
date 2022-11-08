from aiogram import Bot, Dispatcher, executor, types
import asyncio
import logging
import psycopg2

from QRParse.GetOrder import OrderWithStr
from QRParse.QrAPI import OrderWithPhoto

token = "5682324905:AAGxjmZcV36GnnhPp5DSa9NYnz_kqTTM63Y"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=token)

dp = Dispatcher(bot)


# @dp.message_handler()
# async def echo(message: types.Message):
#     answer = f'Уважаю тебя {message.from_user.username}'
#     await message.answer(answer)
#     print(f'От: {message.from_user.username} | Сообщение: {message.text} | Ответ: {answer}')


@dp.message_handler(commands=['data'])
async def orders(message: types.Message):
    conn = psycopg2.connect(dbname='FROFY', user='SA',
                            password='SA', host='localhost')
    cursor = conn.cursor()
    cursor.execute('select * from Товары')
    records = cursor.fetchall()
    await message.answer(f'{records}')
    conn.close()


@dp.message_handler(commands=['orders'])
async def orders(message: types.Message):
    orders = OrderWithStr('t=20221102T1352&s=89.99&fn=9960440301834413&i=6073&fp=1929603051&n=1')
    await message.answer(f'Название: {orders[0]}\nКоличество: {orders[2]}\nЦена: {orders[1]}р')


@dp.message_handler(commands=['qrcode'])
async def orders(message: types.Message):
    orders = OrderWithPhoto()
    await message.answer(orders["data"]["json"]["items"][0]["name"])

# @dp.message_handler(commands=['help'])
# async def start_fn(message: types.Message):
#    await message.answer(message.from_user.id)
