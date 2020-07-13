raph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

# print(graph['start'].keys())  # Для получения всех соседей начального узла.

# Включаем в граф остальные узлы и их соседей:
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = {}  # У конечного узла нет соседей.

# создаем таблицы стоимостей costs:
infinity = float('inf')  # Бесконечнсть
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

# для родителей также создаем отдельную таблицу:
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

# Делаем массив для отслежывания всех уже обработаных узлов, так как один узел не должен обрабатыватся многократно.
processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:  # перебераем все узлы.
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            # Если это узел с наименьшей  стоимостью из уже виденных и он еще не был обработан...
            lowest_cost = cost  # ... он назначается новым узлом с наименьшей стоимостью.
            lowest_cost_node = node
    return lowest_cost_node



# Переходим к алгоритму
node = find_lowest_cost_node(costs)  # Находим узел с найменьшей стоимостью среди необработынных
while node is not None: # Если обработаны все узлы, цикл while завершен.
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():  # Перебираем всех соседей текущего узла.
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:  # если к соседу можно добратся быстрее через текущий узел.
            costs[n] = new_cost    # обновляем стоимость для этого узла.
            parents[n] = node  # этот узел становится новым родителем для соседа.
    processed.append(node)  # Узел помечается как обработанный
    node = find_lowest_cost_node(costs)  # Найти следующий узел для  обработки и повторить цыкл.

print("Cost from the start to each node:")
print(costs)
