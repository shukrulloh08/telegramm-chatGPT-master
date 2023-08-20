# Серверная часть Telegram-бота для ChatGPT.


По мотивам [ChatGPT OpenAI в Telegram на Python / Пишем Telegram-бота ChatGPT на Питоне](https://www.youtube.com/watch?app=desktop&v=7X1zxEzQGGM).

Серверная часть Telegram-бота, использующего [OpenAI ChatGPT](https://chat.openai.com) для генерации ответов на сообщения.

# Установка

Для работы бота потребуется установить Python 3 и несколько пакетов:
```
pip install aiogram openai
```

# Использование

Чтобы запустить бота, необходимо получить токен для бота у [BotFather в Telegram](https://t.me/BotFather), а также [API-ключ для OpenAI](https://platform.openai.com/account/api-keys). Эти значения необходимо передать в качестве аргументов при запуске бота:

```
python main.py <telegram_bot_token> <openai_api_key>
```

# Примечания

Бот сохраняет последние 10 сообщений, которые ему были отправлены, для использования в качестве контекста при генерации ответов. Сохранение сообщений происходит в памяти, без использования базы данных.