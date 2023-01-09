from bot_config import dp, bot
from aiogram import types

total = 150

@dp.message_handler(commands=['start'])#Декоратор, изменяет поведение функции не изменяя функции
async def start_bot(message: types.Message):
    await bot.send_message(message.from_user.id, text = f'{message.from_user.first_name} Ты написал мне {message.text}')


@dp.message_handler() 
async def start_bot(message: types.Message): #Объект класса Месседж
    global total
    if message.text.isdigit():
        total -= int(message.text)
        if 0 < int(message.text) < 29:
            await bot.send_message(message.from_user.id, f'{message.from_user.first_name} взял со стола {message.text} конфет. На столе осталось {total}')
    
    

    #print(f'{message.from_user.id} - {message.from_user.username}') 