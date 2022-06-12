"""
1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
    |--settings
    |--mainapp
    |--adminapp
    |--authapp
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как
лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена
папок под конкретный проект; можно ли будет при этом расширять конфигурацию и хранить
данные о вложенных папках и файлах (добавлять детали)?
"""


import os


# path_to_create_folders = input('Введите путь, куда добавить стартер: ')
path_to_create_folders = 'E:/Python_pr/lesson/Seventh_lesson' #Заменить на предыдущую строку для универсальности
folder_structure_in_str = str()
with open('Starter_configuration.txt', encoding='utf-8') as f:
    folder_structure_in_str = f.read()

path_dict = dict()
path_dict[0] = path_to_create_folders

for i in range(1, folder_structure_in_str.count('|') + 1): #Количество папок вместе
    number_of_tabs = folder_structure_in_str.index('|') #Количество табуляций
    if '\n' in folder_structure_in_str:
        folder_name = folder_structure_in_str[folder_structure_in_str.index('-') + 2: folder_structure_in_str.index('\n')] #Имя папки
    else:
        folder_name = folder_structure_in_str[folder_structure_in_str.index('-') + 2:]  #Имя папки (если в документе не выполнили последний перенос на новую строку)

    if folder_name not in os.listdir(path_dict[number_of_tabs]): #Проверка на наличие папки в данном пути
        os.mkdir(f'{path_dict[number_of_tabs]}/{folder_name}')
    path_dict[int(number_of_tabs + 1)] = f'{path_dict[number_of_tabs]}/{folder_name}'

    if '\n' in folder_structure_in_str:
        folder_structure_in_str = folder_structure_in_str[folder_structure_in_str.index('\n') + 1:]
    else:
        folder_structure_in_str = ''

print('Ready')

""" Напоследок - сложная
2. *(вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей
структурой:
|--my_project
|--settings
| |--__init__.py
| |--dev.py
| |--prod.py
|--mainapp
| |--__init__.py
| |--models.py
| |--views.py
| |--templates
| |--mainapp
| |--base.html
| |--index.html
|--authapp
| |--__init__.py
| |--models.py
| |--views.py
| |--templates
| |--authapp
| |--base.html
| |--index.html
Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом
текстовом редакторе «руками» (не программно); предусмотреть возможные исключительные
ситуации, библиотеки использовать нельзя.
"""


import os
import yaml

structure = """|--my_project
 |--settings
  |--__init__.py
  |--dev.py
  |--prod.py
 |--mainapp
  |--__init__.py
  |--models.py
  |--views.py
  |--templates
  |--mainapp
  |--base.html
  |--index.html
 |--authapp
  |--__init__.py
  |--models.py
  |--views.py
  |--templates
  |--authapp
  |--base.html
  |--index.html"""
# Сколько пробелов, такой и уровень подпапки. Аналогично 1ому заданию
with open('config.yaml', 'w') as f:
    f.write(yaml.dump(structure))

# path_to_create_folders = input('Введите путь, куда добавить стартер: ')
path_to_create_folders = 'E:/Python_pr/lesson/Seventh_lesson' # Заменить на предыдущую строку для универсальности
with open('config.yaml', encoding='utf-8') as f:
    folder_structure_in_str = yaml.safe_load(f)

# print(folder_structure_in_str)
path_dict = dict()
path_dict[0] = path_to_create_folders

for i in range(1, folder_structure_in_str.count('|') + 1): # Количество папок/файлов вместе
    number_of_tabs = folder_structure_in_str.index('|') # Количество табуляций
    if '\n' in folder_structure_in_str:
        folder_name = folder_structure_in_str[folder_structure_in_str.index('-') + 2: folder_structure_in_str.index('\n')] # Имя папки/файла
    else:
        folder_name = folder_structure_in_str[folder_structure_in_str.index('-') + 2:]  # Имя папки/файла (если в документе не выполнили последний перенос на новую строку)

    if folder_name not in os.listdir(path_dict[number_of_tabs]):  # Проверка на наличие папки в данном пути
        if "." in folder_name:
            with open(f'{path_dict[number_of_tabs]}/{folder_name}', 'w') as f:
                f.write('')
        else:
            os.mkdir(f'{path_dict[number_of_tabs]}/{folder_name}')
    path_dict[int(number_of_tabs + 1)] = f'{path_dict[number_of_tabs]}/{folder_name}'

    if '\n' in folder_structure_in_str:
        folder_structure_in_str = folder_structure_in_str[folder_structure_in_str.index('\n') + 1:]
    else:
        folder_structure_in_str = ''

print('Ready')

"""
3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или
«руками» в проводнике).
Написать скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
...
|--templates
| |--mainapp
| | |--base.html
| | |--index.html
| |--authapp
| |--base.html
| |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы
расположены в родительских папках (они играют роль пространств имён); предусмотреть
возможные исключительные ситуации; это реальная задача, которая решена, например, во
фреймворке django.
"""


import os
import shutil


my_dir = 'templates'  # создание папки
if not os.path.exists(my_dir):
    os.mkdir(my_dir)

folder = r'my_project'  # в какой папке искать
files_for_copy = []


for root, dirs, files in os.walk(folder):
    for file in files:
        if '.html' in file:
            files_for_copy.append(os.path.join(root, file))
for path_to_files in files_for_copy:
    folder_new = os.path.join(my_dir, os.path.basename(os.path.dirname(path_to_files)))#Путь: папка, куда сохранять + подпапка для файла
    if not os.path.exists(folder_new):
        os.mkdir(folder_new)
    save_path = os.path.join(folder_new, os.path.basename(path_to_files)) # Путь, куда копировать файл
    shutil.copy(path_to_files, save_path)

"""
4. Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором
ключи — верхняя граница размера файла (пусть будет кратна 10), а значения — общее
количество файлов (в том числе и в подпапках), размер которых не превышает этой границы,
но больше предыдущей (начинаем с 0), например:
{
100: 15,
1000: 3,
10000: 7,
100000: 2
}
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
"""

import os


path_for_stat = 'E:\Python_pr\lesson'
folder_statistics = {}
for root, dirs, files in os.walk(path_for_stat):
    for file in files:
        file_name = f'{root}/{file}'
        file_stats = os.stat(file_name)
        key_for_dict = len(str(file_stats.st_size))
        if pow(10, key_for_dict) in folder_statistics:
            folder_statistics[pow(10, key_for_dict)] = folder_statistics[pow(10, key_for_dict)] + 1
        else:
            folder_statistics[pow(10, key_for_dict)] = 1
print(folder_statistics)

"""
5. *(вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря,
в котором ключи те же, а значения — кортежи вида (<files_quantity>,
[<files_extensions_list>]), например:
{
100: (15, ['txt']),
1000: (3, ['py', 'txt']),
10000: (7, ['html', 'css']),
100000: (2, ['png', 'jpg'])
}
Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили
скрипт.
"""


import os
import json


path_for_stat = 'E:\Python_pr\lesson'
folder_statistics = {
    100: [0,set()],     #1
    1000: [0,set()],    #2
    10000: [0,set()],   #3
    100000: [0,set()],  #4
    1000000: [0,set()], #5
    10000000: [0,set()],#6
    100000000: [0,set()]#7
}
for root, dirs, files in os.walk(path_for_stat):
    # print(root, "- путь", "---", dirs, "- подкаталоги", "--", files, "- файлы")
    for file in files:
        file_name = f'{root}/{file}'
        file_stats = os.stat(file_name)
        _, file_extension = os.path.splitext(file_name)
        if file_stats.st_size <= 100:           #1
            folder_statistics[100][0] = folder_statistics[100][0] + 1
            folder_statistics[100][1].add(file_extension)
        elif file_stats.st_size <= 1000:        #2
            folder_statistics[1000][0] = folder_statistics[1000][0] + 1
            folder_statistics[1000][1].add(file_extension)
        elif file_stats.st_size <= 10000:       #3
            folder_statistics[10000][0] = folder_statistics[10000][0] + 1
            folder_statistics[10000][1].add(file_extension)
        elif file_stats.st_size <= 100000:      #4
            folder_statistics[100000][0] = folder_statistics[100000][0] + 1
            folder_statistics[100000][1].add(file_extension)
        elif file_stats.st_size <= 1000000:     #5
            folder_statistics[1000000][0] = folder_statistics[1000000][0] + 1
            folder_statistics[1000000][1].add(file_extension)
        elif file_stats.st_size <= 10000000:    #6
            folder_statistics[10000000][0] = folder_statistics[10000000][0] + 1
            folder_statistics[10000000][1].add(file_extension)
        elif file_stats.st_size <= 100000000:   #7
            folder_statistics[100000000][0] = folder_statistics[100000000][0] + 1
            folder_statistics[100000000][1].add(file_extension)
for key, val in folder_statistics.items():
    val[1] = list(val[1])
    val = tuple(val)
    print(f'up to {key} bytes, total {val[0]} files, all extensions: {val[1]}')
folder_statistics_for_json = json.dumps(folder_statistics)

with open('E:/Python_pr/lesson/Seventh_lesson/folder_name_summary.json', 'w', encoding='utf-8') as f:
    f.write(folder_statistics_for_json)
