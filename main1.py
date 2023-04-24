from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters import Text
import requests

TOKEN_BOT = "5650923273:AAHNw_En8C4IL5T1k25-z6Lrb5jlNr_B2VE"

bot = Bot(token=TOKEN_BOT)
dp = Dispatcher(bot)


btn1 = KeyboardButton("💬 Задать вопрос")

btn2 = KeyboardButton("ℹ️ Информация")
main_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(btn1, btn2)

@dp.message_handler(commands=["start"])
async def start_cmd(message: types.Message):
    await bot.send_message(message.from_user.id,
    f"""
Привет, @{message.from_user.username}!
Я могу дать тебе пару советов по твоим вопросам.

Что бы передвигать по боту используйте меню 👇.
    """, reply_markup=main_kb)
    
    
btnback1 = KeyboardButton("⬅️ Назад")
back_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(btnback1)
    
@dp.message_handler(Text(equals="⬅️ Назад"))
async def Buy_btn(message: types.Message):
    await bot.send_message(message.from_user.id,f"Вы вернулись в главное меню", reply_markup=main_kb)
    
@dp.message_handler(Text(equals="💬 Задать вопрос"))
async def Buy_btn(message: types.Message):
    await bot.send_message(message.from_user.id,
    f"""
Напиши свой вопрос, задачу, пример и т.д!
    """, reply_markup=back_kb)
    
@dp.message_handler(Text(equals="ℹ️ Информация"))
async def Buy_btn(message: types.Message):
    await bot.send_message(message.from_user.id,
    f"""
Создатель бота - @AiogramMod
Тема бота:
Давать ответы на ваши Вопросы, Задачи, Примеры и т.п..
    """)
  
    




if __name__ == '__main__':
    executor.start_polling(dp)