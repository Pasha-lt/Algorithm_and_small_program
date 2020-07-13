# Selection sort (сортировка выбором) – суть алгоритма заключается в проходе по массиву от начала до конца 
# в поиске минимального элемента массива и перемещении его в начало. Сложность такого алгоритма O(n2).
# first solution
def selection_sort(list_a):

    for i in range(0, len(list_a)-1):
        min_value = i

        for j in range(i+1, len(list_a)):
            if list_a[j] < list_a[min_value]:
                min_value = j

        if min_value !=i:
            list_a[min_value], list_a[i] = list_a[i], list_a[min_value]

    return list_a
print(selection_sort([3,1,10,7,1]))

exit()



# second solution
list_b = []


def selection_sort(list_a):
    sd = 100
    for i in range(0, len(list_a)):
        if list_a[i] < sd:
            sd = list_a[i]
            index = i
    list_b.append(list_a.pop(index))

    if len(list_a) == 0:
        print(list_b)
    else:
        selection_sort(list_a)


selection_sort([6, 3, 1, 5, 4])

exit()
#from book

# Finds the smallest value in an array
def findSmallest(arr):
  # Stores the smallest value
  smallest = arr[0]
  # Stores the index of the smallest value
  smallest_index = 0
  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest_index = i
      smallest = arr[i]
  return smallest_index

# Sort array
def selectionSort(arr):
  newArr = []
  for i in range(len(arr)):
      # Finds the smallest element in the array and adds it to the new array
      smallest = findSmallest(arr)
      newArr.append(arr.pop(smallest))
  return newArr

print(selectionSort([5, 3, 6, 2, 10]))

