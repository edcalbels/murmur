import asyncio
import aioschedule

from aiogram import types, Dispatcher
from config import bot

async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await bot.send_message(chat_id=message.chat.id, text="Got your id")

async  def go_to_sleep():
    await bot.send_message(chat_id=chat_id, text="Пора спать ")



async def wake_up():
    file = open("media/ph.jpg", "rb")
    print(file)
    await bot.send_photo(chat_id=chat_id, photo=file, caption="wakeup")





async def sheduler():
    # aioschedule.every().day.at('19:45').do(go_to_sleep)
    # aioschedule.every().day.at('20:13').do(wake_up)
    aioschedule.every().friday.at('15:70').do(wake_up)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)

def register_handler_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id, lambda word: 'старт' in word.text)


