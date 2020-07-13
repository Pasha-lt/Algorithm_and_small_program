# По условиям задачи нам нужно найти продавца манго, им является человек у которого имя заканчивается на 'm'
from collections import deque  # импортируем для создание двустороней очереди(дека)

def person_is_seller(name):
      return name[-1] == 'm'

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []  # В этот массив будем добавлять людей которых мы уже проверили.
    while search_queue:  # Пока очередь не пуста.
        person = search_queue.popleft()  # Из очереди извлекается первый человек.
        if person not in searched:  # Что бы не попасть в рекурсию смотрим проверяли ли мы человека раньше.
            # peggy дружит с двумя и если не будет проверки то из-за нее попадем в рекурсию
            if person_is_seller(person):  # Проверяем является ли этот человек продавцом манго.
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)  # Добавляем человека в список уже проверенных людей.
    return False

search("you")  # если мы передадим
