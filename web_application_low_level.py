import socket


URLS = {
    '/': 'hello index', # Для корневого будет ответ hello index
    '/blog': 'hello blog',
}


def parse_request(request):
    parset = request.split(' ')
    method = parset[0] # так как у нас первым в строке будет метод(get, post), а вторым юрл то так их и присваиваем.
    url = parset[1]
    return (method, url)


def generate_headers(method, url):
    if not method == 'GET': #Если метод не GET
        return ('HTTP/1.1 405 Method not allowed\n\n', 405)

    if not url in URLS: #будем использовать словарь для хранения урлов и если его нет у нас возвращаем 404
        return ('HTTP/1.1 404 Not found\n\n', 404)

    else:
        return ('HTTP/1.1 200 OK\n\n', 200) # Если все нормально возвращаем 200


def generate_content(code, url):
    if code == 404:
        return '<h1>404</h1><p>Not found</p>'
    if code == 405:
        return '<h1>405</h1><p>Method not allowed</p>'
    return '<h1>{}</h1>'.format(URLS[url])


def generate_response(request):
    method, url = parse_request(request) #Распарсим наш реквест, получим шттп метод и юрл запрос.
    headers, code = generate_headers(method, url) #Тут у нас певым будет заголовок вторым код запроса
    body = generate_content(code, url)    # Генерация тела ответа
    return (headers + body).encode()


def run():
    '''создаем субьект который будет принимать запрос'''
    # AF(adress family) INET(это ip4), ip6 = INET6. socket.SOCK_STREAM - указывает на то что мы берем TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 1-й обращаемся к нашему сокету 2-й повторно разрешаем использование сокет и пишем 3-й True(1)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Связываем наш субьект с конкретным сервером и портом 127.0.0.1 = localhost. можно было написать и localhost
    server_socket.bind(('127.0.0.1', 5000))
    server_socket.listen() # даем серверу указание чтобы он прослушивал наш порт на входящие пакеты.

    while True: # так мы не знаем сколько длится сессия делаем ее зацикленной.
        # медот эксепт возвращает то что он получил от клиента. (передает кортеж из двух элементов сокета и адресса)
        client_socket, addr = server_socket.accept()
        request = client_socket.recv(1024) #смотрим что нам прислал клиент recv выводит информацию указываем в байтах
        print(request) # Запрос можно декодировать (request.decode('utf-8'))
        print()
        print(addr)

        response = generate_response(request.decode('utf-8'))# Функция которая будет отвечать клиенту

        client_socket.sendall(response) # Отвечаем клиенту
        client_socket.close() # Для того чтобы нам что-то увидеть нам нужно закрыть клиентский сокет.


if __name__ == '__main__':
    run()

