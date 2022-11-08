from aiogram import Bot, Dispatcher, executor, types

from Telegram.Bot import dp


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
