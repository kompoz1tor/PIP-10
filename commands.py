from bot_config import dp, bot
from aiogram import types
import random
from random import randint

total = 150
new_game = False
# Функция, которая выполняет вычитание конфет в ход бота
async def bot_turn(message):
    global total
    if total > 28:
        take = random.randint(1,28)
    else:
        take = total
    total -= take
    await bot.send_message(message.from_user.id,f'Бот взял со стола {take} конфет. На столе осталось {total} конфет')


async def player_turn(message):
    name = message.from_user.first_name
    await bot.send_message(message.from_user.id, f'{name} , твой черёд.')
    

#Декоратор, изменяет поведение функции не изменяя функции
@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    global new_game
    new_game = True
    await bot.send_message(message.from_user.id, 
                            text = f'{message.from_user.first_name} привет, ты написал мне {message.text}, мы начинаем игру, сколько конфет ты возьмёшь?')

@dp.message_handler() 
async def start_bot(message: types.Message): #Объект класса Месседж
    global total
    global new_game
    name = message.from_user.first_name
    text = message.text
    if new_game:
        if message.text.isdigit():
            if 0 < int(message.text) < 29:
                total -= int(message.text)
                await bot.send_message(message.from_user.id,
                                        f'{name} взял со стола {text} конфет. На столе осталось {total}')
            else:
                await message.reply(f'{message.from_user.first_name} да ты жадина! Нужно брать  до 29 конфет')  
        else:    
            await bot.send_message(message.from_user.id,
                                        f'{name} напиши сколько ты хочешь взять конфет цифрами, а не вот это вот всё!')
    await bot_turn(message)
    await player_turn(message)


    
    

    #print(f'{message.from_user.id} - {message.from_user.username}') 