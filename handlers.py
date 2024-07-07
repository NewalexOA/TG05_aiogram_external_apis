from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from api_requests import text_to_speech
import logging
import base64
import os

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Привет! Я бот, который может конвертировать текст в речь. Используйте команду /tts для начала.")
    logging.info("Started bot")


@router.message(Command(commands=["help"]))
async def help(message: Message):
    help_text = (
        "Этот бот умеет выполнять следующие команды:\n"
        "/start - Запустить бота\n"
        "/help - Получить помощь по командам бота\n"
        "/tts - Конвертировать текст в речь\n"
    )
    await message.answer(help_text)


@router.message(Command(commands=["tts"]))
async def tts(message: Message):
    await message.answer("Введите текст для конвертации в речь:")


@router.message()
async def handle_message(message: Message):
    user_text = message.text
    audio_content = await text_to_speech(user_text)

    if audio_content:
        audio_data = base64.b64decode(audio_content)
        audio_path = "audio.ogg"
        with open(audio_path, "wb") as audio_file:
            audio_file.write(audio_data)
        await message.answer_voice(types.FSInputFile(audio_path))
        os.remove(audio_path)
    else:
        await message.answer("Не удалось конвертировать текст в речь. Попробуйте снова позже.")


def register_handlers(dp):
    dp.include_router(router)
