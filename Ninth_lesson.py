"""
1. Создать класс TrafficLight (светофор): (делать последней)
● определить у него один атрибут color (цвет) и метод running (запуск);
● атрибут реализовать как приватный;
● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
зелёный;
● продолжительность первого состояния (красный) составляет 7 секунд, второго
(жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
● переключение между режимами должно осуществляться только в указанном порядке
(красный, жёлтый, зелёный);
● проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
import time


class TrafficLight:
    __color = ''

    @staticmethod
    def running():
        sec = 0
        while True:
            start = time.perf_counter()
            if sec == 0:
                __color = "red"
                print(__color, sec)
                start = time.perf_counter()
                time.sleep(7)
                end_red = time.perf_counter()
                sec = round(end_red - start)
                print(sec)
            if sec == 7:
                __color = "yellow"
                print(__color, sec)
                time.sleep(2)
                end_ye = time.perf_counter()
                sec = round(end_ye - start)
                print(sec)
            if sec == 9:
                __color = "green"
                print(__color, sec)
                time.sleep(7)
                end_green = time.perf_counter()
                sec = round(end_green - start)
                print(sec)
            if sec == 16:
                sec = 0


my_traffic_light = TrafficLight()
my_traffic_light.running()

"""
2. Реализовать класс Road (дорога). +
● определить атрибуты: length (длина), width (ширина); +
● значения атрибутов должны передаваться при создании экземпляра класса; +
● атрибуты сделать защищёнными; +
● определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
● использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
дороги асфальтом, толщиной в 1 см*число см толщины полотна;
● проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""


class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass_calculation(self, asphalt_mass_for_1_m2, height):
        asphalt_mass = self._length * self._width * asphalt_mass_for_1_m2 * height
        return asphalt_mass


road = Road(20, 5000)
print(f'{road.asphalt_mass_calculation(25, 5)/1000} т')

"""
3. Реализовать базовый класс Worker (работник):
● определить атрибуты: name, surname, position (должность), income (доход);
● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
элементы «оклад» и «премия», например, {"wage": wage, "bonus": bonus};
● создать класс Position (должность) на базе класса Worker;
● в классе Position реализовать методы получения полного имени сотрудника
(get_full_name) и дохода с учётом премии (get_total_income);
● проверить работу примера на реальных данных: создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            'wage': wage,
            'bonus': bonus
        }


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        total_income = self._income['wage'] + self._income['bonus']
        return total_income


human1 = Position('Алиса', 'Эль', 'Актриса', 150000, 250000)
print(human1.get_full_name())
print(human1.get_total_income())

"""
4. Реализуйте базовый класс Car:
● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). +
А также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда); +
● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;+
● добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;+
● для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости. +
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Вызовите методы и покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Машина едет со скоростью {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Вы превысили скорость! Ваша скорость сейчас: {self.speed} км/ч')
        else:
            print(f'Машина едет со скоростью {self.speed} км/ч')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Вы превысили скорость! Ваша скорость сейчас: {self.speed} км/ч')
        else:
            print(f'Машина едет со скоростью {self.speed} км/ч')


class PoliceCar(Car):
    pass


my_car = TownCar(45, 'red', 'flower')
my_car_too = WorkCar(45, 'blue', 'sunshine')

print(f'About my car {my_car.name}: colour is {my_car.color}, speed is {my_car.speed}. That is police car? '
      f'{my_car.is_police}.')
my_car.go()
my_car.stop()
my_car.turn('Влево')
my_car.show_speed()

print(f'About my car {my_car_too.name}: colour is {my_car_too.color}, speed is {my_car_too.speed}. That is police car? '
      f'{my_car_too.is_police}.')
my_car_too.go()
my_car_too.stop()
my_car_too.turn('Влево')
my_car_too.show_speed()

"""
5. Реализовать класс Stationery (канцелярская принадлежность):
● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
сообщение «Запуск отрисовки»;+
● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);+
● в каждом классе реализовать переопределение метода draw. Для каждого класса
метод должен выводить уникальное сообщение;
● создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    @staticmethod
    def draw():
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        super
        print('Ручка пишет хорошо')


class Pencil(Stationery):
    def draw(self):
        super
        print('Карандаш пишет хорошо')


class Handle(Stationery):
    def draw(self):
        super
        print('Маркер пишет хорошо')


my_pen = Pen('princess')
my_pencil = Pencil('kitti')
my_handle = Handle('honey')

print(my_pen.title)
my_pen.draw()
print(my_pencil.title)
my_pencil.draw()
print(my_handle.title)
my_handle.draw()
