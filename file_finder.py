import fnmatch
import shutil
from datetime import datetime
import os

# path_work_dir = os.getcwd() # путь к текущей папке
# print(path_work_dir)

# устанавливаем путь к текущей рабочей папке в нашем случае это /home/admin2/Desktop
os.chdir(r'/home/admin2/Desktop')


# Получаем os.listdir('.') список файлов в текущей папке. текущую директорию можна сменить os.chdir
for fname in os.listdir('.'):
    # выводим файлы с расширением py
    if fnmatch.fnmatch(fname, '*.py'):
        print(fname)

# walk() принимает имя каталога и последовательно его проходит возвращая обьект генератора.
for root, dirs, files in os.walk(r'/home/admin2/Desktop/Важное_дубль_на_флешку/Программирование'):
    for name in files:
        fullname = os.path.join(root, name)
        # print(fullname)
        if('.md' in fullname):  # выводим все файлы с расширением md
            print(fullname)

# Узнаем размер файла и дату его можификации.
path = r'/home/admin2/Desktop/2.jpg'
# получаем размер файла в байтах
size = os.path.getsize(path)
ksize = size//1024
atime = os.path.getatime(path) # Дата последнего чтения
mtime = os.path.getmtime(path) # Дата последнего редактирования

print(f'Размер: {ksize} KB')
print(f'Дата последнего использования: {datetime.fromtimestamp(atime)}')
print(f'Дата последнего редактирования: {datetime.fromtimestamp(mtime)}')
