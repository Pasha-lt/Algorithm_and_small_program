# была поставлена задача проверить список что у него следующий елемент больше или равен предведущему.
# Метод должен вернуть True False

def old_function(list_a):
    for num in range(len(list_a) - 1):
        if float(list_a[num]) >= list_a[num + 1]:
            return False
        else:
            return True


def function_with_enumarate(list_a):
    for num, element in enumerate(list_a[:-1]):
        if list_a[num] >= list_a[num + 1]:
            return False
        else:
            return True


def short_version(list_a):
    result = [list_a[1], *list_a] >= list_a
    return result

def check_throght_sort(list_a):
    return list_a == sorted(list_a)

assert old_function([0, 1, 23, 567]) == True
# assert old_function([1, 1, 1, 1]) == True  # Он сломается, если будут одинаковые цифры
# assert old_function([]) == False # пустой список тоже сломает
assert old_function([0, 1, 23, 567, 1004, 20898]) == True
assert old_function([909, 915, 2020]) == True
assert old_function([57, 1, 23, 14, 28]) == False
assert old_function([57, 1, 23, 14, 36, 28]) == False
assert old_function([100, 23, 1]) == False
print(1)
assert function_with_enumarate([0, 1, 23, 567]) == True
assert function_with_enumarate([0, 1, 23, 567, 1004, 20898]) == True
assert function_with_enumarate([909, 915, 2020]) == True
assert function_with_enumarate([57, 1, 23, 14, 28]) == False
assert function_with_enumarate([57, 1, 23, 14, 36, 28]) == False
assert function_with_enumarate([100, 23, 1]) == False
print(2)
assert short_version([0, 1, 23, 567]) == True
assert short_version([0, 1, 23, 567, 1004, 20898]) == True
assert short_version([909, 915, 2020]) == True
assert short_version([57, 1, 23, 14, 28]) == False
assert short_version([57, 1, 23, 14, 36, 28]) == False
assert short_version([100, 23, 1]) == False
print(3)
assert check_throght_sort([0, 1, 23, 567]) == True
assert check_throght_sort([0, 1, 23, 567, 1004, 20898]) == True
assert check_throght_sort([909, 915, 2020]) == True
assert check_throght_sort([57, 1, 23, 14, 28]) == False
assert check_throght_sort([57, 1, 23, 14, 36, 28]) == False
assert check_throght_sort([100, 23, 1]) == False
print(4)
