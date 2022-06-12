"""
1. Написать функцию email_parse(<email_address>), которая при помощи регулярного
выражения извлекает имя пользователя и почтовый домен из email адреса и возвращает их в
виде словаря. Если адрес не валиден, выбросить исключение ValueError.
Пример:
# >>> email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
...
raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru

Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном
выражении; имеет ли смысл в данном случае использовать функцию re.compile()?
"""
import re


RE_EMAIL = re.compile(r'^(?P<username>[a-zA-Z0-9_.+-]+)@(?P<domain>[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)$')


def email_parser(email_address):
    result_match_object = RE_EMAIL.match(email_address)
    if result_match_object is None:
        raise ValueError(f'wrong email: {email_address}')
    return result_match_object.groupdict()


email_address_for_parse = input('Введите почтовый ящик: ')
result_dict = email_parser(email_address_for_parse)
print(result_dict)

"""
2. *(вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6
урока nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
для получения информации вида: (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, 
<response_code>, <response_size>),

например:
raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET/downloads/product_2 HTTP/1.1" 304 0 "-" 
"Debian APT-HTTP/1.3 (0.9.7.9)"'
parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET','/downloads/product_2', '304', '0')

Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле?
Были ли особенные строки? Можно ли для них уточнить регулярное выражение?
"""
import re
import requests


RE_REMOTE_ADDR = re.compile(r'(?:[\d]{1,3}\.){3}[\d]{1,3}')
RE_REQUEST_DATETIME = re.compile(r'[\d]{2}\/[a-zA-Z]+\/[\d]{4}(?::[\d]{2}){3}\s\+[\d]{4}')
RE_REQUEST_TYPE = re.compile(r'"(?P<request_type>[A-Z]{2,})')

RE_REQUEST_RESOURCE = re.compile(r' (?P<requested_resource>(?:\/[\w ]*){2,}[\w]) HTTP')
RE_RESPONSE_CODE = re.compile(r' (?P<response_code>[\d]{3}) ')
RE_REQUESTED_RESOURCE = re.compile(r' (?P<response_size>[\d]{1,5}) "')

url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
r = requests.get(url)
with open('nginx_logs.txt', 'w') as file:
    file.write(r.text)

with open('nginx_logs.txt', 'r', encoding='utf-8') as file:
    number_line = 0
    for line in file:
        number_line = number_line + 1
        print(number_line)
        print('удаленный адрес: ', RE_REMOTE_ADDR.findall(line), 'запрос даты и времени: ', RE_REQUEST_DATETIME.findall(line))
        print('тип запроса: ', RE_REQUEST_TYPE.findall(line), 'запрошенный ресурс: ', RE_REQUEST_RESOURCE.findall(line))
        print('код ответа: ', RE_RESPONSE_CODE.findall(line), 'размер ответа: ', RE_REQUESTED_RESOURCE.findall(line))

"""
3. Написать декоратор для логирования типов позиционных аргументов функции, например:

def type_logger...
...
@type_logger
def calc_cube(x):
return x ** 3
>>> a = calc_cube(5)
5: <class 'int'>

Примечание: 
если аргументов несколько - выводить данные о каждом через запятую? 
можете ли вы вывести тип значения функции? 
Сможете ли решить задачу для именованных аргументов?
Сможете ли вы замаскировать работу декоратора? 
Сможете ли вывести имя функции, например, в виде:
calc_cube(5: <class 'int'>)
"""
from functools import wraps


def type_logger(func):

    @wraps(func)
    def wrapper(*args):
        result = []
        for arg in args:
            result.append(func(arg))
            print(f'{arg}: {type(arg)}')
        print(f'{func}: {type(func)}')
        return result
    return wrapper


@type_logger
def calc_cube(x):
    """Function here"""
    return x ** 3


list_values = [5, 7, 8]
a = calc_cube(*list_values)

for i in range(0, len(list_values)):
    print(f'{calc_cube.__name__}({list_values[i]}): {a[i]}')
print(calc_cube.__doc__)
"""
4. Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные
значения функции и выбрасывать исключение ValueError, если что-то не так, например:

def val_checker...
...
@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3
    
>>> a = calc_cube(5)
125
>>> a = calc_cube(-5)
Traceback (most recent call last):
...
raise ValueError(msg)
ValueError: wrong val -5

Примечание: сможете ли вы замаскировать работу декоратора?
"""
from functools import wraps


def val_checker(argument_func): #Сюда передается лямбда

    def logger(func): #Сюда передается функция calc_cube

        @wraps(func)
        def wrapper(*args): #Сюда передаются аргументы функции - x (5)
            result = []
            for arg in args:
                if argument_func(arg) is False:
                    raise ValueError(f'wrong val {arg}')
                result.append(func(*args))
            return result

        return wrapper

    return logger


@val_checker(lambda x: x > 0) #Возвращает True or False
def calc_cube(x):
    """ Function here """
    return x ** 3


a = calc_cube(17)
print(a)
print(calc_cube.__doc__)

