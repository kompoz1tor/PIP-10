from aiogram.utils import executor # Импортируем эекзекютер. Исполнитель
from commands import dp

# В функцт. bot_start нужно передать атрибут неважно какой
async def bot_start(_): 
    print('Бот запущен!')

# Метод start_polling начинает прослушивание
# skip_updates=True Бот пропускает все данные пока не включится
executor.start_polling(dp, skip_updates=True, on_startup = bot_start)