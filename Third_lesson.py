"""
1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
Например:
>>> num_translate("one")
"один"
>>> num_translate("eight")
"восемь"
Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую
для перевода: какой тип данных выбрать, в теле функции или снаружи.
"""


def num_translate(en_word):
    dictionary = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять',
    }
    if en_word in dictionary:
        print(dictionary[en_word])
        return dictionary[en_word]
    else:
        return None


english_word = input('Введите слово на английском: ')
num_translate(english_word)

"""
2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу
с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
>>> num_translate_adv("One")
"Один"
>>> num_translate_adv("two")
"два"
"""


def num_translate_adv(en_word):
    dictionary = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять',
    }
    if en_word in dictionary:
        print(dictionary[en_word])
        return dictionary[en_word]
    elif en_word == en_word.title() and en_word.lower() in dictionary:
        en_word = en_word.lower()
        print(dictionary[en_word].title())
        return dictionary[en_word].title()
    else:
        return None


english_word = input('Введите слово на английском: ')
num_translate_adv(english_word)

# Или пополнить словарь

"""
3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
Например:
>>>  thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"],
    "М": ["Мария"], "П": ["Петр"]
}
Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется сортировка по ключам?
Можно ли использовать словарь в этом случае?
"""


def thesaurus(*args):
    dictionary = {}
    for name in args:
        letter = name[:1]
        if letter in dictionary:
            dictionary[letter].append(name)
        else:
            new_key_arg = {letter: [name]}
            dictionary.update(new_key_arg)
    return dictionary


list_names = input('Введите имена сотрудников через пробел: ').split()
dict_name = thesaurus(*list_names)
print(dict_name)


"""
4. * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки
в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари,
реализованные по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей
буквы. Например:
>>>thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": ["Петр Алексеев"]
    },
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"],
        "А": ["Анна Савельева"]
    }
}
Как поступить, если потребуется сортировка по ключам?
"""


def thesaurus_adv(*args):
    dictionary = {}
    for full_name in args:
        name, last_name = full_name.split()
        letter_last_name = last_name[:1]
        letter_name = name[:1]
        if letter_last_name in dictionary:
            if letter_name in dictionary[letter_last_name]:
                dictionary[letter_last_name[letter_name]].append(full_name)
            else:
                new_key_arg_inside = {letter_name: full_name}
                dictionary[letter_last_name].update(new_key_arg_inside)
        else:
            new_key_arg = {letter_last_name: {letter_name: full_name}}
            dictionary.update(new_key_arg)
    return dictionary


list_names = input('Введите имена сотрудников через запятую (Имя Фамилия): ').split(', ')
dict_name = thesaurus_adv(*list_names)
print(dict_name)

"""
5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
взятых из трёх списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
        Например:
>>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]
Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
(когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
"""

import random


def get_jokes(n):
    """ Генератор шуток"""
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    i = 0
    jokes = []
    while i < n:
        joke = f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}'
        jokes.append(joke)
        i += 1
    return jokes


print(get_jokes(int(input('Введите нужное количество шуток: '))))
