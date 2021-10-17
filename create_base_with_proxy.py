import requests
from bs4 import BeautifulSoup
import re


def check_proxy(list_proxy):
    work_proxy = []
    for number, proxy in enumerate(list_proxy):
        url = 'http://' + proxy
        try:
            response = requests.get('https://www.google.com/', proxies={'http': url})
            if response.status_code == 200:
                # print(f'{url} рабочий юрл {number}')
                work_proxy.append(proxy)
        except requests.exceptions.ConnectionError:
            print(url, 'нерабочий юрл')
            continue
    return work_proxy

def get_ip_list():
    HEADERS = {
        'User-Agent': 'user agent'
    }
    URL = 'url'
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('tr', class_='spy1xx')
    items_2 = soup.findAll('tr', class_='spy1x')
    items = str(items) + str(items_2)
    
    ip_list_with_scum = items.split('class')
    ip_list = []
    for in_str in ip_list_with_scum:
        m = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?:\:\d{1,5})?)', in_str)
        if m:
            ip_list.append(m.group(0))
    return check_proxy(ip_list)
