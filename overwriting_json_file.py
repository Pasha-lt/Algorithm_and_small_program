import json
from random import choice

def gen_person():
    '''function to generate content'''
    name = ''
    tel = '+38093'
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    while len(name) != 5:
        name += choice(letters)
    while len(tel) != 13:
        tel += choice(nums)
    person = {
        'name': name,
        'tel': tel
    }
    return person

def write_json(person_dict):
    try:
        data = json.load(open('persons.json')) # открывайем для чтения файл - 'open('persons.json')',
    except: # если такого файла нет то создаем его
        data = []
    data.append(person_dict) # расширяем наш файл полученым словарем - person_dict
    with open('persons.json', 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False) # в этот раз дополняем его списком обьектов(посути перезаписываем).


def main():

    for i in range(5): # generate 5 blocks.
        write_json(gen_person())




if __name__ == '__main__':
    main()