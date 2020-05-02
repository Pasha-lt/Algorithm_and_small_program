# Для того чтобы установить счетчик на функцию вешаем на нее декоратор @timeit
from datetime import datetime


def timeit(func):
   def wrapper(*args, **kwargs): # если не знаем какие аргументы функция принимает добавляем args, kwargs
       start = datetime.now()  # Засекает текущее время
       result = func(*args, **kwargs) #запускаем нашу функцию
       print(datetime.now() - start) #вызываем еще раз время и отнимаем замер до функции.
       return result
   return wrapper
