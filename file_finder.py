import os
import fnmatch

# Возвращаем путь к текущей папке
path_work_dir = os.getcwd()
print(path_work_dir)

# устанавливаем путь к текущей рабочей папке в нашем случае это /home/admin2/Desktop/Важное_дубль_на_флешку
# os.chdir(r'/home/admin2/Desktop/Важное_дубль_на_флешку/Программирование')

# Получаем os.listdir('.') список файлов в текущей папке. текущую директорию можна сменить os.chdir
for fname in os.listdir('.'):
    # выводим файлы с расширением py
    if fnmatch.fnmatch(fname, '*.py'):
        print(fname)
