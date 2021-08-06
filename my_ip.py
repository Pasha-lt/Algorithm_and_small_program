import requests


def my_ip():
    """функция выводит IP пользователя."""
    r = requests.get('http://httpbin.org/ip') # Командой get отправляем запрос на указаный сайт.
    my_ip = r.json()['origin'] # Данные у нас в JSON декодируем и берем ключ 'origin'.
    return f'Ваш IP-адрес - {my_ip}'


a = my_ip()
print(a)
