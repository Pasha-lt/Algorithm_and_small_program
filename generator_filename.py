from time import time

def gen_filename():
    """Бесконечный генератор для генерации названия файлов"""
    while True:
        t = int(time()*1000000)  # Время в секундах с начала эпои Unix
        yield f'{t}.jpg'


p = gen_filename()
print(next(p))
print(next(p))