"""
4. Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания. Создать скрипт,
в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates(). Убедиться, что ничего
лишнего не происходит.
5. * (вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли.
"""
import currency_converter
import time
import sys


argv = sys.argv[1:]
desired_currency = argv[0]
final_currency, today_date = currency_converter.currency_rates(desired_currency)
if final_currency == None:
    print('Такой валюты нет в списке, попробуйе еще раз.')
    time.sleep(5)
else:
    print(f'1 RUB = {final_currency} {desired_currency}\nДата курса: {today_date}')
    time.sleep(5)
