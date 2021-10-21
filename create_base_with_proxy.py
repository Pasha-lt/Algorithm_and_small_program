import requests
from bs4 import BeautifulSoup
import re


def check_proxy(list_proxy):
    """Метод проверяет рабочее ли прокси на вход принимает лист со всеми прокси возвращает лист
    с рабочими прокси"""
    work_proxy = []  # создаем пустой список куда будем наполнять рабочие прокси
    # проходим списком по листу всех прокси, чтобы определить какие рабочие какие нет.
    for number, proxy in enumerate(list_proxy):
        try:
            # Отправляем запрос через прокси и сохраняем его в переменую respone  
            response = requests.get('https://www.google.com/',
                                    proxies={'http': proxy, 'https': proxy}, timeout=5)
            # проверяем статус код ответа если он 200 то добавляем в нас список прокси
            if response.status_code == 200:
                work_proxy.append(proxy)
        except requests.exceptions.ConnectionError:
            # если мы поймали исключение тогда юрл не сохраняем
            print(proxy, 'нерабочий юрл')
            continue
    return work_proxy  # возвращаем список рабочих юрлов.


def get_ip_list():
    """функция парсит сайт и достает с него все proxy"""
    # Используем юзер агент чтобы сайт нас не блокировал как бота.
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }
    
    URL = ''  # юрл сайта который мы будем парсить
    # отправляем запрос на сайт, сохраняем ответ в переменую что бы в дальнейшем его спарсить.
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('tr', class_='spy1xx')
    items_2 = soup.findAll('tr', class_='spy1x')
    items = str(items) + str(items_2)
    
    ip_list_with_scum = items.split('class')
    ip_list = []
    for in_str in ip_list_with_scum:
        # используем регулярку чтобы достать айпи и порт
        m = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?:\:\d{1,5})?)', in_str)
        if m:
            ip_list.append(m.group(0))
    return check_proxy(ip_list)
