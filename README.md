
### [Описание на русском языке](#русский)

### [Description in English](#english)

---

## <a name="русский"></a>Описание на русском языке

### Описание

Этот учебный проект представляет собой Telegram-бота, который взаимодействует с внешними API для преобразования текста в речь.

### Функциональность бота

#### Преобразование текста в речь

- Пользователь отправляет текст, который он хочет преобразовать в аудио.
- Бот использует внешнее API для преобразования текста в аудио формат.
- Аудио файл отправляется пользователю в ответ на его сообщение.
- После отправки аудио файл удаляется.

### Установка и запуск

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/NewalexOA/TG05_aiogram_external_apis.git
   ```

2. Перейдите в директорию проекта:
   ```bash
   cd TG05_aiogram_external_apis
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

   4. Создайте файл конфигурации `config.py` и добавьте ваши токены. Для получения RAPIDAPI_KEY зарегистрируйтесь на [RapidAPI](https://rapidapi.com/rahilkhan224/api/text-to-speech-neural-google) и подпишитесь на нужный API сервис:
      ```plaintext
      BOT_TOKEN = 'your_telegram_bot_token'
      RAPIDAPI_KEY = 'your_rapidapi_key'
      ```

5. Запустите бота:
   ```bash
   python main.py
   ```

---

## <a name="english"></a>Description in English

### Description

This educational project is a Telegram bot that interacts with external APIs to convert text to speech.

### Bot Functionality

#### Text to Speech Conversion

- The user sends text that they want to convert to audio.
- The bot uses an external API to convert the text to an audio format.
- The audio file is sent back to the user in response to their message.
- The audio file is deleted after sending.

### Installation and Run

1. Clone the repository:
   ```bash
  git clone https://github.com/NewalexOA/TG05_aiogram_external_apis.git
   ```

2. Navigate to the project directory:
   ```bash
   cd TG05_aiogram_external_apis
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `config.py` configuration file and add your tokens. To obtain a RAPIDAPI_KEY, register on [RapidAPI]([RapidAPI](https://rapidapi.com/rahilkhan224/api/text-to-speech-neural-google)) and subscribe to the required API service:
   ```plaintext
   BOT_TOKEN = 'your_telegram_bot_token'
   RAPIDAPI_KEY = 'your_rapidapi_key'
   ```

5. Start the bot:
   ```bash
   python main.py
   ```