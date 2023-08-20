import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import sys

token = input('Enter your bot token:') 

openai.api_key = input('Enter your openai api key:') 

bot = Bot(token)
dp = Dispatcher(bot)

# Словарь для хранения контекста
context = {}

@dp.message_handler()
async def send(message : types.Message):
    if not message.text:  # проверка на пустой текст сообщения
        return
    
    chat_id = message.chat.id
    
    # Создаем список сообщений для данного чата, если его еще нет
    if chat_id not in context:
        context[chat_id] = []
    
    # Добавляем текущее сообщение в список
    context[chat_id].append(message.text)
    
    # Ограничиваем длину списка 10 элементами
    context[chat_id] = context[chat_id][-10:]
    
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = "Context:\n" + "\n".join(context[chat_id]) + "\nPrompt:\n" + message.text,
        temperature = 0.9,
        max_tokens = 1000,
        top_p = 1.0,
        frequency_penalty = 0.0,
        presence_penalty = 0.6,
        stop=[" Human:", " AI:"])
    
    await message.answer(response['choices'][0]['text'])
    
executor.start_polling(dp, skip_updates=True)
