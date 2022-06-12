"""
1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield,
например:
>>> odd_to_15 = odd_nums(15)
>>> next(odd_to_15)
1
>>> next(odd_to_15)
3
...
>>> next(odd_to_15)
15
>>> next(odd_to_15)
...StopIteration...
"""


def odd_nums_gen(maxi):
    for num in range(1, maxi + 1, 2):
        yield num


max_num = int(input('Введите верхнюю границу интервала: '))
odd_nums = odd_nums_gen(max_num)
upper_limit = max_num // 2 + 1
for i in range(1, upper_limit + 1):
    print(next(odd_nums))

"""
# 2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя
# ключевое слово yield.
"""

max_num = int(input('Введите верхнюю границу интервала: '))
odd_nums = (num for num in range(1, max_num + 1, 2))
upper_limit = max_num // 2 + 1
for i in range(1, upper_limit + 1):
    print(next(odd_nums))

"""
3. Есть два списка:
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
('Иван', '9А')
('Анастасия', '7В')
...
Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в списке klasses меньше
элементов, чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None), например:
('Станислав', None)

### Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения. Подумать, в каких
ситуациях генератор даст эффект.
"""

import random


def add_el_from_lists(name, klass):
    for y in range(0, len(name) + 1):
        if len(klass) < len(name):
            diff_ce = len(name) - len(klass)
            for z in range(0, diff_ce):
                klass.append(None)
        result = list()
        result.append(name[y])
        result.append(klass[y])
        result = tuple(result)
        yield result


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
random.shuffle(tutors)
random.shuffle(klasses)
gen_name_klass = add_el_from_lists(tutors, klasses)
for i in range(1, len(tutors) + 1):
    print(next(gen_name_klass))

"""
4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего,
например:
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]
```

Подсказка: использовать возможности python, изученные на уроке.
"""

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result1 = []
for i in range(1, len(src)):
    if src[i] > src[i - 1]:
        result1.append(src[i])
print(result1)

result2 = []
result2 = [src[i] for i in range(1, len(src)) if src[i] > src[i-1]]
print(result2)

"""
5. Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать из этих элементов
список с сохранением порядка их следования в исходном списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.
"""


import time


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

# В лоб
start1 = time.perf_counter_ns()
for i in src:
    if src.count(i) != 1:
        for j in range(1, src.count(i) + 1):
            src.remove(i)
end1 = time.perf_counter_ns()
print(end1-start1)
print(src)

# Оптимизация
unique_num = list()
additionally = set()
start2 = time.perf_counter_ns()
for el in src:
    if el not in additionally:
        unique_num.append(el)
    else:
        unique_num.discard(el)
    additionally.add(el)
end2 = time.perf_counter_ns()
print(round(end2-start2, 10))
print(unique_num)

