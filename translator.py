from googletrans import Translator
translator = Translator()
""" 
"transl_from.txt" - файл с текстом который нужно перевести.
"text_result.txt" - переведенный текст. 
src - язык текста который переводим.
dest - язык текста на который переводим.
en - Английский
ru - Русский
uk - Украинский
Больше языков https://cloud.google.com/translate/docs/languages
"""

with open ("before.txt", 'r', encoding='utf-8') as file1:
    k = file1.read()

k = translator.translate(k, src='en', dest='uk').text

with open("after.txt", 'w') as file2:
    file2.write(k)

