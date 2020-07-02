# Составим список штатов, используем множества.
states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])  # Передаем масив и преобразуем его в множество.

# Составляем список станций. Используем словари, ключи - станции, а значение - сокращенные обозначения покрытых штатов.
stations = {}
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])

final_stations = set()  # Структура данных для хранения итогового набора станций.


while states_needed:
    best_station = None  # Станция которая обслуживает больше всего штатов невходящее в текущее покрытие.
    states_covered = set()

    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station  # пересечение множеств.
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    final_stations.add(best_station)
    states_needed -= states_covered  # обновляем содержимое states_needed продолжаем пока оно не станет пустым.

print(final_stations)
