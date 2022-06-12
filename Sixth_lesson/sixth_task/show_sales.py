"""
Реализовать простую систему хранения данных о суммах продаж булочной. Должно быть два скрипта с интерфейсом
командной строки: для записи данных и для вывода на экран записанных данных.

Для чтения данных реализовать в командной строке следующую логику:

просто запуск скрипта — выводить все записи;
запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер, равный
второму числу, включительно.

Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1.
"""

def main(argv):
    _, *args = argv

    if len(args) == 0:
        with open('bakery.csv', 'r', encoding='utf-8') as f:
            print(f.read())

    else:
        counter = 1
        i = False
        with open('bakery.csv', 'r', encoding='utf-8') as f:

            if len(args) == 1:
                for line in f:
                    if counter == int(args[0]):
                        i = True
                    if i is True:
                        print(line[:-1])
                    counter += 1

            if len(args) == 2:
                for line in f:
                    if counter == int(args[0]):
                        i = True
                    if i is True:
                        print(line[:-1])
                    if counter == int(args[1]):
                        i = False
                    counter += 1



if __name__ == '__main__':
   import sys


   main(sys.argv)