import requests
from bs4 import BeautifulSoup
import re


HEADERS = {
    'User-Agent': 'user_agent'
}
URL = 'site'
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

print(ip_list)
