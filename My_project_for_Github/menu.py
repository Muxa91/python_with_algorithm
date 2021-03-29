import sys
import arithmetic_progression
import pascals_triangle
import tetration
import conversion_time
import conversion_curency
import tasks_list
import task_dict
import task_strings


class LoggingPrinter:

    def __init__(self):
        self.out_file = open('My_log.txt', "w")
        self.old_stdout = sys.stdout
        # этот объект возьмет на себя работу `stdout`
        sys.stdout = self

    # Выволняется, когда пользователь выполняет 'input'

    def input(self, text):
        print(text, end=' ')
        arg = sys.stdin.readline()
        self.out_file.write(arg)
        return str(arg)

    def flush(self):
        pass

    # выполняется, когда пользователь выполняет `print`
    def write(self, text):
        self.old_stdout.write(text)
        self.out_file.write(text)

    # выполняется, когда начинается блок `with`
    def __enter__(self):
        return self

    # выполняется, когда блок `with` заканчивается

    def __exit__(self, type, value, traceback):
        # Восстановление исходного объекта stdout.
        sys.stdout = self.old_stdout


def input(text):
    arg = LoggingPrinter().input(text)
    return arg

user_name = input("Здравствуйте, как к Вам обращаться\n")

class Menu:

    with LoggingPrinter():
        __user_name = user_name
        def start_program(self):

            while True:

                if self.__user_name.isspace() == True or self.__user_name == '':
                    self.__user_name = input("Необходимо ввести имя\n")
                    continue
                if len(self.__user_name) < 50:

                    break
                else:
                    self.__user_name = str(input("Введите имя короче\n"))
                    continue
            self.main_menu()

        def main_menu(self):
            while True:
                try:
                    print(
                        "\nГлавное меню\n" + self.__user_name + 'с чем хотете поработать?\n1)Завершение программы\n'
                                                                '2)работа с списками словарями кортежами множествами\n3)математические модели')
                    user_act = int(input('введите номер действия\n'))
                    if user_act == 1:
                        print("Всего доброго")
                        break
                    elif user_act == 2:
                        self.menu_list_str_dict_set()
                        break
                    elif user_act == 3:
                        self.menu_mathematical_models()
                        break
                    else:
                        print('Введите цифру из предоставленных действий')
                except ValueError:
                    print('необходимо ввести цифру')

        def menu_after_task(self, repeat, back):
            while True:
                try:

                    print("\n\nВыберте дальнейшие действия\n1)повторить\n9)назад\n0)Главное меню")
                    user_act = int(input('введите номер действия\n'))
                    if user_act == 1:
                        print("Вы выбрали повторить")
                        eval(repeat)
                        print(repeat)

                        break
                    elif user_act == 9:
                        print("Назад")
                        eval(back)
                        break
                    elif user_act == 0:
                        self.main_menu()
                        exit()
                    else:
                        print('Введите цифру из предоставленных действий')
                except ValueError:
                    print('необходимо ввести цифру')  # FIX!!!!#FIX!!!!

        def menu_mathematical_models(self):
            while True:
                try:
                    print(self.__user_name + ',', 'Вы выбрали математические модели с чем хотите поработать?\n'
                                                  '1)Арифметическая прогрессия\n'
                                                  '2)Треугольник Паскаля\n'
                                                  '3)Тетрация\n'
                                                  '4)Конвертер времени\n'
                                                  '5)Ковертор валют\n 9)назад\n0)завершение работы')
                    user_act = int(input('введите номер действия\n'))
                    if user_act == 1:
                        arithmetic_progression.Arithmetic_progression().output_range()
                        break
                    elif user_act == 2:
                        pascals_triangle.Pascals_triangle().triangle()
                        break
                    elif user_act == 3:
                        tetration.Tetration().tetration()
                        break
                    elif user_act == 4:
                        conversion_time.ConversionTime().conversion()
                        break
                    elif user_act == 5:
                        conversion_curency.ConversionCurrency().converter()
                        break
                    elif user_act == 9:
                        self.main_menu()
                        break
                    elif user_act == 0:
                        exit()
                    else:
                        print('Введите цифру из предоставленных действий')

                except ValueError:
                    print('необходимо ввести цифру')

        def menu_list_str_dict_set(self):
            while True:
                try:
                    print(self.__user_name +
                          'Вы выбрали работу со списками, словарями, строками.C чем хотите поработать?'
                          '\n1)Списки \n2)Словари \n3)Строки\n 9)назад \n0)завершение работы')
                    user_act = int(input('введите номер действия\n'))
                    if user_act == 1:
                        self.menu_list()
                        break

                    elif user_act == 2:
                        self.menu_dict()
                        break

                    elif user_act == 3:
                        self.menu_string()
                        break

                    elif user_act == 9:
                        self.main_menu()
                        break

                    elif user_act == 0:
                        exit()

                    else:
                        print('Введите цифру из предоставленных действий')

                except ValueError:
                    print('необходимо ввести цифру')

        def menu_list(self):
            while True:
                try:
                    print(self.__user_name +
                          'Вы выбрали работу со списками. Что Вы хотите с ними сделать?'
                          '\n1)Вывести все элементы, которые меньше 5'
                          '\n2)Вернуть список, который состоит из элементов, общих для  двух списков.'
                          '\n3)Составить список и кортеж с задаными числами'
                          '\n4)Вывести первый и последний элемент списка'
                          '\n5)Вывести чётные числа из заданного списка и останавиться, если встречает число 237'
                          '\n6)выводести все элементы первого списка, которых нет во второмсписке'
                          '\n7)извлечь из списка числа, делимые на 15'
                          '\n8)проверить, все ли числа в последовательности уникальны'
                          '\n9)назад'
                          '\n0)завершение работы')
                    user_act = int(input('введите номер действия\n'))
                    if user_act == 1:
                        tasks_list.Tasks_lists().find_less_than_five()
                        break
                    elif user_act == 2:
                        tasks_list.Tasks_lists().find_common_elements()
                        break
                    elif user_act == 3:
                        tasks_list.Tasks_lists().make_list_tuple()
                        break
                    elif user_act == 4:
                        tasks_list.Tasks_lists().find_first_last_elemets()
                        break
                    elif user_act == 5:
                        tasks_list.Tasks_lists().find_even_numbers()
                        break
                    if user_act == 6:
                        tasks_list.Tasks_lists().find_differences()
                        break
                    elif user_act == 7:
                        tasks_list.Tasks_lists().find_multiple_15()
                        break
                    elif user_act == 8:
                        tasks_list.Tasks_lists().check_uniqueness()
                        break
                    elif user_act == 9:
                        self.menu_list_str_dict_set()
                        break
                    elif user_act == 0:
                        exit()
                    else:
                        print('Введите цифру из предоставленных действий')

                except ValueError:
                    print('необходимо ввести цифру')

        def menu_dict(self):
            while True:
                try:
                    print(self.__user_name +
                          'Вы выбрали работу со словарями. Что Вы хотите с ними сделать?'
                          '\n1)Отсортировать словарь по значению в порядке возрастания и убывания'
                          '\n2)сделать слияние нескольких словарей в один.'
                          '\n3)Найти три ключа с самыми высокими значениями в словаре'
                          '\n9)назад'
                          '\n0)завершение работы')
                    user_act = int(input('введите номер действия\n'))
                    if user_act == 1:
                        task_dict.Tasks_dict().sort_dict()
                        break

                    elif user_act == 2:
                        task_dict.Tasks_dict().merger_two_dict()
                        break

                    elif user_act == 3:
                        task_dict.Tasks_dict().find_three_max_values()
                        break

                    elif user_act == 9:
                        self.menu_list_str_dict_set()
                        break

                    elif user_act == 0:
                        exit()
                    else:
                        print('Введите цифру из предоставленных действий')

                except ValueError:
                    print('необходимо ввести цифру')

        def menu_string(self):
            while True:
                try:
                    print(self.__user_name +
                          'Вы выбрали работу со строками. Что Вы хотите с ними сделать?'
                          '\n1)вывести два слова из текста: наиболее часто встречающееся и самое длинное.'
                          '\n2)Посчитать, сколько раз символ встречается в строке.'
                          '\n3)определить является ли слова палиндромом'
                          '\n9)назад'
                          '\n0)завершение работы')
                    user_act = int(input('введите номер действия\n'))
                    if user_act == 1:
                        task_strings.Tasks_string().find_long_and_frequent()
                        break

                    elif user_act == 2:
                        task_strings.Tasks_string().find_symbol()
                        break

                    elif user_act == 3:
                        task_strings.Tasks_string().find_palindrome()
                        break

                    elif user_act == 9:
                        self.menu_list_str_dict_set()
                        break

                    elif user_act == 0:
                        exit()
                    else:
                        print('Введите цифру из предоставленных действий')

                except ValueError:
                    print('необходимо ввести цифру')


# if __name__ == '__main__':
#     with LoggingPrinter():
#         Menu().start_program()
