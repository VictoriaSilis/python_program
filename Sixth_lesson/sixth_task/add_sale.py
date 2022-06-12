"""
Реализовать простую систему хранения данных о суммах продаж булочной. Должно быть два скрипта с интерфейсом
командной строки: для записи данных и для вывода на экран записанных данных.

При записи передавать из командной строки значение суммы продаж.
Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1.
"""

def main(argv):
    _, args = argv
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.write(f'{args}\n')


if __name__ == '__main__':
   import sys


   main(sys.argv)