from aiogram import Bot, types
from aiogram.types import ChatActions
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import StatesGroup, State
from config import TOKEN
from states import UserData as ud

from aiogram.dispatcher import FSMContext
import keyboard as kb
import models

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)


def func1(arg: str):
    return models.get_congr(arg)


def func2(arg: str):
    return models.get_news(arg)


func_dict = {'Добро': func1, 'Зло': func2}


@dp.message_handler(commands=['start'], state='*')
async def process_start_command(message: types.Message):
    await message.reply("Привет, я Саня текстач, умею генерировать тексты! Что генерируем?", reply_markup=kb.greet_kb11)
    await ud.style.set()


@dp.message_handler(state=ud.style)
async def dobro_zlo(msg: types.Message, state: FSMContext):
    text = msg.text
    if text not in ['Добро', 'Зло']:
        await msg.reply("Выбери Добро или Зло", reply_markup=kb.greet_kb11)
        await ud.style.set()

    else:
        await state.update_data(style=text)
        await msg.reply('Напиши текст')
        await ud.text.set()


@dp.message_handler(state=ud.text)
async def text_handler(msg: types.Message, state: FSMContext):
    text = msg.text
    print(text)
    async with state.proxy() as data:
        style = data['style']

    res = func_dict[style](text)
    print(res)

    await bot.send_chat_action(msg.chat.id, ChatActions.TYPING)
    await msg.reply(res, reply_markup=kb.greet_kb11)
    await ud.style.set()


if __name__ == '__main__':
    executor.start_polling(dp)
