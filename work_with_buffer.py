# Подключаем модуль для работы с буфером обмена
import pyperclip
import time

old_value_buffer = ''  # тут будет храниться значение буфера.
while True:
    buffer = pyperclip.paste()  # сохраняем в переменую содержимое буфера.
    #если у нас новые данные в буфере перезаписываем их
    if old_value_buffer != buffer:
        print(buffer)
        old_value_buffer = buffer
        with open('clipboard.txt', 'a', encoding='utf8' ) as file:
            file.write(buffer + '\n')
        #Проверяем копированое сообщение на наличие собачки, если оно там есть то возможно это почта.
        if '@' in buffer:
            # перезаписываем в буфер нашу строку.
            pyperclip.copy('Вы попытались вставить почту но мы ее подминили')
            
        
        
    # Делаем паузу чтобы содержимое буфера успело прогрузиться.
    time.sleep(1)
