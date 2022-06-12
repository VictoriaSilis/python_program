"""
2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты(например, USD, EUR,
+GBP, ...) и возвращающую курс этой валюты по отношению к рублю.
Можно ли, используя только методы класса str, решить поставленную задачу? Функция должна возвращать результат
числового типа, например float.
Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
Сильно ли усложняется код функции при этом?
Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент? В качестве
примера выведите курсы доллара и евро.
3. * (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату, которая
передаётся в ответе сервера. Дата должна быть в виде объекта date. Подумайте, как извлечь
дату из ответа, какой тип данных лучше использовать в ответе функции?
"""

import requests
from decimal import Decimal
import datetime


def currency_rates(val):
    currency_website = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    currency_website = currency_website.text
    val = val.upper()

    start_data_of_today = currency_website.find('<ValCurs Date="') + 15
    str_of_data = currency_website[start_data_of_today:]
    end_data_of_today = str_of_data.find('"')
    data_of_today = str_of_data[:end_data_of_today]
    day, month, year = data_of_today.split('.')
    day = int(day)
    month = int(month)
    year = int(year)
    final_data_of_today = datetime.date(year, month, day)

    if val in currency_website:
        first_match_index = currency_website.find(val)
        new_str = currency_website[first_match_index:]

        start_str = new_str.find('<Value>') + 7
        end_str = new_str.find('</Value>')
        currency = new_str[start_str:end_str]
        currency = currency.replace(',', '.')
        currency = Decimal(currency)

        return currency, final_data_of_today
    else:
        return None, None


if __name__ == '__main__':
    print('Все имеющиеся валюты на сайте: AUD - Австралийский доллар, AZN - Азербайджанский манат, GBP - '
      'Фунт стерлингов Соединенного королевства,\nAMD - Армянских драмов, BYN - Белорусский рубль, BGN'
      ' - Болгарский лев, BRL - Бразильский реал, HKD - Гонконгских долларов, DKK - Датская крона,\nUSD'
      ' - Доллар США, EUR - Евро, INR - Индийских рупий, KZT - Казахстанских тенге, CAD - Канадский доллар, '
      'KGS - Киргизских сомов, CNY - Китайский юань,\nMDL - Молдавских леев, NOK - Норвежских крон, PLN - '
      'Польский злотый, RON - Румынский лей, XDR - СДР (специальные права заимствования),\nSGD - '
      'Сингапурский доллар, TJS - Таджикских сомони, TRY - Турецких лир, TMT - Новый туркменский манат,'
      ' UZS - Узбекских сумов, UAH - Украинских гривен,\nCZK - Чешских крон, SEK - Шведских крон, CHF - '
      'Швейцарский франк, ZAR - Южноафриканских рэндов, KRW - Вон Республики Корея, JPY - Японских иен')
    desired_currency = input('Введите валюту, курс которой хотите узнать: ')
    final_currency, today_date = currency_rates(desired_currency)
    if final_currency == None:
        print('Такой валюты нет в списке, попробуйе еще раз.')
    else:
        print(f'1 RUB = {final_currency} {desired_currency}\nДата курса: {today_date}')