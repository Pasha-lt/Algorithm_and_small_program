from gtts import gTTS
ru = 'Привет, я Читаю этот текст!'
tts_ru = gTTS(ru, lang='ru')
with open('test.mp3', 'wb') as f:
    tts_ru.write_to_fp(f)
