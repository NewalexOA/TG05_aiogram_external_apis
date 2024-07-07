
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

### Структура проекта

Проект состоит из следующих файлов и директорий:

- `main.py`: Главный файл для запуска бота. Инициализирует бота и диспетчер, устанавливает команды и запускает опрос обновлений.
- `config.py`: Файл конфигурации, содержащий токены и ключи доступа.
- `handlers.py`: Содержит обработчики команд и сообщений бота.
- `api_requests.py`: Содержит функции для запросов к внешнему API.
- `requirements.txt`: Список зависимостей проекта.


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

### Project Structure

The project consists of the following files and directories:

- `main.py`: The main file for running the bot. It initializes the bot and dispatcher, sets commands, and starts polling for updates.
- `config.py`: Configuration file containing the bot tokens and access keys.
- `handlers.py`: Contains handlers for bot commands and messages.
- `api_requests.py`: Contains functions for making requests to the external API.
- `requirements.txt`: List of project dependencies.

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