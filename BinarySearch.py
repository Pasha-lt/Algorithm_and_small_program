# Алгоритм бинарного поиска. 
# Бинарный поиск это поиск элемента в отсортированном массиве.
# функция будет возращать False если элемент не найдет и номер элемента если он найден.

def binarysearsch(mylist, iskat, start, stop): #Функция принимает лист(где искать), что искать(число), откуда(start) и до куда(stop) искать.
    if start > stop: # возвращаем False если
         return False
    else:
        mid = (start + stop) // 2 #Высчитываем наш mid нам нужно целое число поэтому используем целочисленое деление.
        # вдальнейшем мы будем через mid выражать start и stop
        if iskat == mylist[mid]: # Сравниваем если  iskat равно  mylist[mid] то возвращаем mid
            return mid # mid(также мы можем здесь написать start или stop они совпадают если число есть) У нас при возврате показывает индекс числа
        elif iskat < mylist[mid]: # если цифра которую мы ищем меньше mid
            return binarysearsch(mylist, iskat, start, mid -1) # stop(конечную точку отсчета) будет равен mid - 1 и делаем пересчет
        else:
            return binarysearsch(mylist, iskat, mid + 1, stop) # start(начальную точку отсчета) будет равен mid + 1 и делаем пересчет

mylist = [10, 12, 13, 15, 20, 24, 27, 33, 42, 51, 57, 68, 70, 77, 79, 81] # Список в котором будем делать поиск.
iskat = 33 # указываем какую цыфру ищем.
start = 0 # ставим индекс с которого мы начинаем искать первый элемент
stop = len(mylist) # конец списка - длина листа.

x = binarysearsch(mylist, iskat, start, stop) #вызов функции.

if x == False: #проверка если числа нет то пишем что его нет.
    print('Item', iskat, 'Not found!')
else: # иначе пишем его индекс(если нашли).
    print('Item', iskat, 'Found at index', x)
    
 exit()

#from book

def binary_search(list, item):
  # low and high keep track of which part of the list you'll search in.
  low = 0
  high = len(list) - 1

  # While you haven't narrowed it down to one element ...
  while low <= high:
    # ... check the middle element
    mid = (low + high) // 2
    guess = list[mid]
    # Found the item.
    if guess == item:
      return mid
    # The guess was too high.
    if guess > item:
      high = mid - 1
    # The guess was too low.
    else:
      low = mid + 1

  # Item doesn't exist
  return None

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3)) # => 1

# 'None' means nil in Python. We use to indicate that the item wasn't found.
print(binary_search(my_list, -1)) # => None
