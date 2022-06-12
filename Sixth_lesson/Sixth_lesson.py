""""
1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера
nginx_logs.txt
получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]
Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
"""

final_list = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        remote_addr = line[:line.index(' ')]
        line = line[line.index(']') + 3:]
        request_type = line[:line.index(' ')]
        line = line[line.index('/'):]
        requested_resource = line[:line.index(' ')]
        variable_tuple = (remote_addr, request_type, requested_resource)
        final_list.append(variable_tuple)
for el in final_list:
    print(el)

"""
2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего
задания.
Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами, размер
которых превышает объем ОЗУ компьютера.
"""
import time

list_of_addr = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        remote_addr = line[:line.index(' ')]
        list_of_addr.append(remote_addr)

# 1 решение (самое плохое):
# a = 0
# number_of_spammer_times = list_of_addr.count(list_of_addr[0])
# spammers_addr = list_of_addr[0]
# for el in list_of_addr:
#     a = list_of_addr.count(el)
#     if a > number_of_spammer_times:
#         spammers_addr = el
#         number_of_spammer_times = a
# print(spammers_addr, number_of_spammer_times)  #216.46.173.126 2350

# 2 решение (плохое):
# start_1 = time.perf_counter()
# not_unique_addr = set()
# all_addr = set()
# for el in list_of_addr:
#     if el not in all_addr:
#         not_unique_addr.discard(el)
#     else:
#         not_unique_addr.add(el)
#     all_addr.add(el)
#
# not_unique_addr_list = list(not_unique_addr)
# a = 0
# number_of_spammer_times = list_of_addr.count(not_unique_addr_list[0])
# spammers_addr = not_unique_addr_list[0]
# for el in not_unique_addr_list:
#     a = list_of_addr.count(el)
#     if a > number_of_spammer_times:
#         spammers_addr = el
#         number_of_spammer_times = a
# print(spammers_addr, number_of_spammer_times) #216.46.173.126 2350
# end_1 = time.perf_counter()
# print(end_1-start_1) #1.3086867

# 3 решение (итоговое):
start_2 = time.perf_counter()
dict_of_addr = {}
for el in list_of_addr:
    if el in dict_of_addr:
        dict_of_addr[el] = dict_of_addr[el] + 1
    else:
        dict_of_addr[el] = 1

max_val = 1
ip_of_max_val = ''
for key, val in dict_of_addr.items():
    if val > max_val:
        max_val = val
        ip_of_max_val = key
print(ip_of_max_val, max_val) #216.46.173.126 2350
end_2 = time.perf_counter()
print(end_2-start_2) #0.010106199999999843


"""
3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Известно, что при
хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая.
Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о
хобби. Сохранить словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей,
чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1». При решении задачи
считать, что объём данных в файлах во много раз меньше объема ОЗУ.
"""


import json


# Обработка данных ФИО
with open('users.csv', 'r', encoding='utf-8') as f:
    users_str = f.read()
users = users_str.split('\n')
for el in range(0, len(users)):
    users[el] = users[el].replace(',', ' ')

# Обработка данных хобби
with open('hobby.csv', 'r', encoding='utf-8') as f:
    hobby_str = f.read()
hobby = hobby_str.split('\n')
for el in range(0, len(hobby)):
    hobby[el] = hobby[el].split(',')

if len(hobby) < len(users):
    for el in range(0, len(users) - len(hobby)):
        hobby.append(None)

dict_of_users_with_hobby = {users[el]: hobby[el] for el in range(0, len(users))}
dict_for_file = json.dumps(dict_of_users_with_hobby)

with open('users_with_hobby.csv', 'w', encoding='utf-8') as f:
    f.write(dict_for_file)

"""
4. * (вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ (разумеется, не нужно
реально создавать такие большие файлы, это просто задел на будущее проекта). Также реализовать парсинг данных из
файлов — получить отдельно фамилию, имя и отчество для пользователей и название каждого хобби: преобразовать в
какой-нибудь контейнерный тип (список, кортеж, множество, словарь). Обосновать выбор типа. Подумать, какие могут
возникнуть проблемы при парсинге. В словаре должны храниться данные, полученные в результате парсинга.
"""


import json


# Обработка данных ФИО - кортеж для ключей в словаре в будущем
users = list()
with open('users.csv', 'r', encoding='utf-8') as f:
    for line in f:
        users.append(line)
for el in range(0, len(users)):
    users[el] = users[el][:-1]
    users[el] = users[el].replace(',', ' ')


# Обработка данных хобби
hobby = list()
with open('hobby.csv', 'r', encoding='utf-8') as f:
    for line in f:
        hobby.append(line)
for el in range(0, len(hobby)):
    hobby[el] = hobby[el][:-1]
    hobby[el] = hobby[el].split(',')
if len(hobby) < len(users):
    for el in range(0, len(users) - len(hobby)):
        hobby.append(None)

dict_of_users_with_hobby = {users[el]: hobby[el] for el in range(0, len(users))}
dict_for_file = json.dumps(dict_of_users_with_hobby)

with open('users_with_hobby.csv', 'w', encoding='utf-8') as f:
    f.write(dict_for_file)

"""
5. ** (вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было задать путь к обоим
исходным файлам и путь к выходному файлу со словарём. Проверить работу скрипта для случая, когда все файлы находятся
в разных папках.
"""


import json
import sys


# Обработка данных ФИО - кортеж для ключей в словаре в будущем
users, hobby, out = sys.argv[1:]
users_list = list()
with open(users, 'r', encoding='utf-8') as f:
    for line in f:
        users_list.append(line)
for el in range(0, len(users_list)):
    users_list[el] = users_list[el][:-1]
    users_list[el] = users_list[el].replace(',', ' ')


# Обработка данных хобби
hobby_list = list()
with open(hobby, 'r', encoding='utf-8') as f:
    for line in f:
        hobby_list.append(line)
for el in range(0, len(hobby_list)):
    hobby_list[el] = hobby_list[el][:-1]
    hobby_list[el] = hobby_list[el].split(',')
if len(hobby_list) < len(users):
    for el in range(0, len(users) - len(hobby_list)):
        hobby_list.append(None)

dict_of_users_with_hobby = {users_list[el]: hobby_list[el] for el in range(0, len(users_list))}
dict_for_file = json.dumps(dict_of_users_with_hobby)

with open(out, 'w', encoding='utf-8') as f:
    f.write(dict_for_file)
