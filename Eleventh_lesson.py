"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""
import random


class Player:
    def __init__(self, players_card):
        if isinstance(players_card, CardForLoto):
            self.players_card = players_card
        else:
            raise ValueError('Неправильный тип карточки')

    def choice_of_move(self):
        choice = input('Хотите зачеркнуть цифру в своей карточке? "y" - да, "n" - нет\n')
        return choice


class Computer:
    def __init__(self, computers_card):
        if isinstance(computers_card, CardForLoto):
            self.computers_card = computers_card
        else:
            raise ValueError('Неправильный тип карточки')

    def choice_of_move(self, number):
        choice = ''
        flag = False
        for i in range(3):
            if number in self.computers_card.my_card[i]:
                flag = True
                index_of_number = self.computers_card.my_card[i].index(number)
                self.computers_card.my_card[i][index_of_number] = '--'
        if flag is True:
            return 'y'
        else:
            return 'n'


class Loto:
    def __init__(self, player, computer):
        self.all_numbers = [x for x in range(1, 91)]
        random.shuffle(self.all_numbers)
        self.count_for_numbs = -1
        if (isinstance(player, Player) and isinstance(computer, Computer)) is False:
            raise ValueError('Неправильный тип игроков')
        self.player = player
        self.computer = computer

    def choose_number(self):
        if self.all_numbers is not None:
            self.count_for_numbs += 1
            final_numb = self.all_numbers[self.count_for_numbs]
            self.all_numbers[self.count_for_numbs:]
            return final_numb
        else:
            return None

    def play(self):
        print(f'Добро пожаловать в игру!\nКарта игрока:\n{self.player.players_card}'
              f'Карта компьютера:\n{self.computer.computers_card}')
        count_player = 15
        count_computer = 15
        break_flag = False

        while count_computer > 0 and count_player > 0:
            number = self.choose_number()
            print(f'Цифра номер {number}')

            answer_player = self.player.choice_of_move()
            print(f'Ответ игрока: {answer_player}')
            answer_computer = self.computer.choice_of_move(number)
            print(f'Ответ компьютера: {answer_computer}')

            if self.check_answer(self.player, answer_player, number) is False:
                break_flag = True
                break

            print(f'Карта игрока:\n{self.player.players_card}\nКарта компьютера:\n{self.computer.computers_card}')
            if answer_player == 'y':
                count_player -= 1
            if answer_computer == 'y':
                count_computer -= 1

        if break_flag is True:
            print('Вы проиграли!')
        elif count_player == 0 and count_computer == 0:
            print('Ничья')
        elif count_player == 0:
            print('Вы выиграли')
        else:
            print('Выиграл компьютер!')

    def check_answer(self, player, answer_player, number):
        pass
        flag = False
        is_right = False
        for i in range(3):
            if number in player.players_card.my_card[i]:
                flag = True

        if (answer_player == 'y') and (flag is True):
            is_right = True
            for i in range(3):
                if number in player.players_card.my_card[i]:
                    index_of_number = player.players_card.my_card[i].index(number)
                    player.players_card.my_card[i][index_of_number] = '--'

        elif (answer_player == 'n') and (flag is False):
            is_right = True

        return is_right


class CardForLoto:
    def __init__(self):
        self._numbs_in_card = []
        self._space_for_card = []
        self.generator()
        self.generator_space()

    def generator(self):
        all_numbs = []
        for x in range(1, 91):
            all_numbs.append(x)
        random.shuffle(all_numbs)
        all_numbs = all_numbs[:15]

        for i in range(3):
            self._numbs_in_card.append(all_numbs[:5])
            self._numbs_in_card[i].sort()
            all_numbs = all_numbs[5:]

    @property
    def my_card(self):
        return self._numbs_in_card

    def generator_space(self):
        for i in range(3):
            index_for_space = [x for x in range(8)]
            random.shuffle(index_for_space)
            self._space_for_card.append(index_for_space[:4])

    def __str__(self):
        list_to_print = []

        for i in range(0, 3):
            numbers_in_list = 5
            for j in range(0, 9):
                if j in self._space_for_card[i]:
                    list_to_print.append(' ')
                else:
                    list_to_print.append(self._numbs_in_card[i][5 - numbers_in_list])
                    numbers_in_list -= 1

        str_to_print = ''

        for i in range(27):
            if len(str(list_to_print[i])) == 1:
                str_to_print = (f'{str_to_print}  {list_to_print[i]}')
            else:
                str_to_print = (f'{str_to_print} {list_to_print[i]}')
            if i == 8 or i == 17:
                str_to_print = (f'{str_to_print}\n')

        return f'---------------------------\n{str_to_print}\n---------------------------\n'


my_card = CardForLoto()
computer_card = CardForLoto()
my_player = Player(my_card)
comp = Computer(computer_card)
loto_1 = Loto(my_player, comp)
loto_1.play()













