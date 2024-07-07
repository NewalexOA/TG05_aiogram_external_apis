import ssl
import certifi
import aiohttp
from config import TTS_API_URL, RAPIDAPI_KEY


async def text_to_speech(text, language='ru-RU'):
    headers = {
        "Content-Type": "application/json",
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": "text-to-speech-neural-google.p.rapidapi.com"
    }
    payload = {
        "audioFormat": "ogg",
        "paragraphChunks": [text],
        "voiceParams": {
            "name": "Wavenet-B",
            "engine": "google",
            "languageCode": language
        }
    }
    ssl_context = ssl.create_default_context(cafile=certifi.where())

    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_context)) as session:
        async with session.post(TTS_API_URL, json=payload, headers=headers) as response:
            if response.status == 200:
                data = await response.json()
                return data.get('audioStream')
            else:
                error_data = await response.text()
                return None
