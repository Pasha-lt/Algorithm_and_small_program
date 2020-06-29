import webbrowser


def save_youtube(url):
    '''Скрипт получает ссылку на видео на ютубе и переводит на страницу где можно его скачать'''
    url = url[:12] +'ss'+ url[12:]
    webbrowser.open(url) # переходим на указанный адрес


url = input('Введите ваш youtube URL: >>>')
save_youtube(url)