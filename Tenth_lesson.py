"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
__init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде
прямоугольной схемы.

Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
31 22
37 43
51 86

3 5 32
2 4 6
-1 64 -8

3 5 8 3
8 3 7 1

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном
виде.
Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой
строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.
"""


class Matrix:
    def __init__(self, list_of_lists):
        self.height = len(list_of_lists)
        self.width = len(list_of_lists[0])
        self.list_of_lists = list_of_lists
        self._check_matrix(self)

    def _check_matrix(self, matrix_to_check):
        for line in matrix_to_check.list_of_lists:
            if matrix_to_check.width != len(line):
                raise ValueError('Неправильно записана матрица')

    def _check_matrix_to_matrix(self, other_matrix):
        self._check_matrix(other_matrix)
        other_width = len(other_matrix.list_of_lists[0])
        other_height = len(other_matrix.list_of_lists)

        if self.width == other_width and self.height == other_height:
            print('true')
            return True
        else:
            print('Матрицы разного размера')
            return False

    def __str__(self):
        final = ''
        for line in self.list_of_lists:
            final += f'{line}\n'
        return final

    def __add__(self, other_matrix):
        flag = False
        if isinstance(other_matrix, Matrix):
            flag = self._check_matrix_to_matrix(other_matrix)
        else:
            raise ValueError('Не класс Matrix')

        if flag is True:
            list_for_matrix = list()

            for i in range(self.height):
                list_for_list = list()
                for j in range(self.width):
                    list_for_list.append(other_matrix.list_of_lists[i][j] + self.list_of_lists[i][j])
                list_for_matrix.append(list_for_list)

            new_matrix = Matrix(list_for_matrix)
            return new_matrix
        else:
            raise ValueError('Нельзя сложить матрицы')


my_list1 = [[1, 2, 2], [1, 1, 1]]
my_list2 = [[3, 2, 2], [1, 1, 1]]
m1 = Matrix(my_list1)
m2 = Matrix(my_list2)
print(m1.list_of_lists)
print(m1)

print(m2.list_of_lists)
print(m2)

m3 = m1.__add__(m2)
print(m3)

"""
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — одежда, которая может иметь определённое название. К
типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H
соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке
знания. Реализовать абстрактные классы для основных классов проекта и проверить работу
декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes:
    total_cost_of_fabric = 0

    def __init__(self, size, growth):
        self.size = size
        self.growth = growth

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):
    @property
    def fabric_consumption(self):
        fabric = round((self.size/6.5 + 0.5), 2)
        Clothes.total_cost_of_fabric += fabric
        return fabric


class Costume(Clothes):
    @property
    def fabric_consumption(self):
        fabric = round((2 * self.growth + 0.3), 2)
        Clothes.total_cost_of_fabric += fabric
        return fabric


my_coat = Coat(40, 150)
my_coat2 = Coat(55, 178)
my_costume = Costume(50, 190)
print(f'{my_coat.fabric_consumption} - ткань на {my_coat.__class__.__name__} с параметрами: размер {my_coat.size}, '
      f'рост {my_coat.growth}')
print(f'{my_coat.total_cost_of_fabric} - по идее глобальный подсчет расхода ткани')
print(f'{my_coat2.fabric_consumption} - ткань на {my_coat2.__class__.__name__} с параметрами: размер {my_coat2.size}, '
      f'рост {my_coat2.growth}')
print(f'{my_coat.total_cost_of_fabric} - по идее глобальный подсчет расхода ткани')

print(f'{my_costume.fabric_consumption} - ткань на {my_costume.__class__.__name__} с параметрами: размер '
      f'{my_costume.size}, рост {my_costume.growth}')
print(f'{my_costume.total_cost_of_fabric} - по идее глобальный подсчет расхода ткани')

"""
3. Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо
создать класс «Клетка». В его конструкторе инициализировать параметр, соответствующий
количеству ячеек клетки (целое число). В классе должны быть реализованы методы
перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
умножение (__mul__()), деление (__floordiv____truediv__()). Эти методы должны применяться
только к клеткам и выполнять увеличение, уменьшение, умножение и округление до целого
числа деления клеток соответственно.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться
сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки. Операцию необходимо выполнять, только если разность
количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.

Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки — произведение
количества ячеек этих двух клеток.

Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как
целочисленное деление количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и
количество ячеек в ряду. Этот метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n
равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний
ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5. В этом
случае метод make_order() вернёт строку: *****\n*****\n**.
Или количество ячеек клетки — 15, а количество ячеек в ряду равняется 5. Тогда метод
make_order() вернёт строку: *****\n*****\n*****.
"""


class Cell:
    def __init__(self, number_of_cells):
        self.number_of_cells = number_of_cells
        self.check_cell(self)

    def __add__(self, other_cell):
        self.check_cell(other_cell)
        new_cell = Cell(self.number_of_cells + other_cell.number_of_cells)
        return new_cell


    def __sub__(self, other_cell):
        self.check_cell(other_cell)
        if (self.number_of_cells - other_cell.number_of_cells) > 0:
            new_cell = Cell(self.number_of_cells - other_cell.number_of_cells)
            return new_cell
        else:
            raise ArithmeticError('Невозможно вычитание. Результат меньше 0')

    def __mul__(self, other_cell):
        self.check_cell(other_cell)
        new_cell = Cell(self.number_of_cells * other_cell.number_of_cells)
        return new_cell

    def __truediv__(self, other_cell):
        self.check_cell(other_cell)
        if (self.number_of_cells // other_cell.number_of_cells) > 0:
            new_cell = Cell(self.number_of_cells // other_cell.number_of_cells)
            return new_cell
        else:
            raise ArithmeticError('Невозможно деление. Результат меньше 0')

    def __floordiv__(self, other_cell):
        self.__truediv__(other_cell)

    def check_cell(self, cell_to_check):
        if isinstance(cell_to_check, Cell):
            if (cell_to_check.number_of_cells > 0) and (isinstance(cell_to_check.number_of_cells, int) is True):
                return True
            else:
                raise ValueError('Количество частей клеток не может быть меньше одной, части клеток могут быть '
                                 'только целым числом')
        else:
            raise TypeError('Вторая переменная не класса Клетка')

    def make_order(self, number_of_cells_in_a_row):
        cell_str = ''
        remainder = number_of_cells_in_a_row - (self.number_of_cells % number_of_cells_in_a_row)
        for i in range(1, self.number_of_cells + remainder + (self.number_of_cells//number_of_cells_in_a_row) + 1):
            if i % (number_of_cells_in_a_row + 1) == 0:
                cell_str += '\n'
            else:
                cell_str += '*'

        return cell_str


c1 = Cell(12)
c2 = Cell(3)
# print((c1+c2).number_of_cells)
# print((c1-c2).number_of_cells)
# print((c1*c2).number_of_cells)
# print((c1/c2).number_of_cells)
print(c1.make_order(1))













