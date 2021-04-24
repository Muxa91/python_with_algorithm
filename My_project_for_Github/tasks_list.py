import menu
import os
class Tasks_lists:
    def __input_nubers(self):
        while True:
            try:
                a = input('Введите список чисел через пробел\n').split(' ')

                for x in a:
                    if x == '':
                        a.remove('')
                    elif int(x) % 1 == 0:
                        pass
                break
            except:
                print('Введите список состящих их чисел')

        return a

    # Выведите все элементы, которые меньше 5.
    def find_less_than_five(self):
        l = self.__input_nubers()
        result = [x for x in l if int(x) < 5]
        print(result)
        menu.Menu().menu_after_task(repeat='tasks_list.Tasks_lists().make_list_tuple().find_less_than_five()',
                                    back='self.menu_list()')
    # Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
    def find_common_elements(self):
        print('Введите первый список')
        a = self.__input_nubers()
        print('Введите второй список')
        b = self.__input_nubers()
        result = [x for x, j in zip(a, b) if x == j]
        print(result)
        menu.Menu().menu_after_task(repeat='tasks_list.Tasks_lists().make_list_tuple().find_common_elements()',
                                    back='self.menu_list()')

    # Вы принимаете от пользователя последовательность чисел, разделённых запятой.
    # Составьте список и кортеж с этими числами.
    def make_list_tuple(self):
        print('составить список и картеж')
        number_list = self.__input_nubers()
        number_tuple = tuple(number_list)
        print("Картеж\n", number_tuple)
        print("Список\n", number_list)
        menu.Menu().menu_after_task(repeat='tasks_list.Tasks_lists().make_list_tuple().make_list_tuple()',
                                    back='self.menu_list()')

    # Выведите первый и последний элемент списка.
    def find_first_last_elemets(self):
        print("Вывести первый и последний элемент списка")
        list1 = self.__input_nubers()
        print("первый элемент",list1[0],"Второй элемент", list[-1])
        menu.Menu().menu_after_task(repeat='tasks_list.Tasks_lists().make_list_tuple().find_first_last_elemets()',
                                    back='self.menu_list()')

    # Напишите программу, которая выводит чётные числа из заданного списка и останавливается, если встречает число 237.
    def find_even_numbers(self):
        list1 = self.__input_nubers()
        print(list1)
        list_result = []
        for x in list1:
            if int(x) % 2 == 0:
                list_result.append(x)
            elif x == 237:
                break
        print(list_result)
        menu.Menu().menu_after_task(repeat='tasks_list.Tasks_lists().make_list_tuple().find_even_numbers()',
                                    back='self.menu_list()')

    # # Напишите программу, которая принимает два списка и выводит все элементы первого, которых нет во втором.
    def find_differences(self):
        print('Написать программу, которая принимает два списка и выводит все элементы первого, которых нет во втором.')
        print('Введите первый список')
        list1 = self.__input_nubers()
        print('Введите второй список')
        list2 = self.__input_nubers()
        print(set(list1) - set(list2))
        menu.Menu().menu_after_task(repeat='tasks_list.Tasks_lists().make_list_tuple().find_differences()',
                                    back='self.menu_list()')

    # С помощью анонимной функции извлеките из списка числа, делимые на 15
    def find_multiple_15(self):
        lists = self.__input_nubers()
        result = list(filter(lambda x: x % 15 == 0, lists))
        print(result)
        menu.Menu().menu_after_task(repeat='tasks_list.Tasks_lists().make_list_tuple().find_multiple_15()',
                                    back='self.menu_list()')

    # Нужно проверить, все ли числа в последовательности уникальны.
    def check_uniqueness(self):
        print('проверить, все ли числа в последовательности уникальны')
        numbers = self.__input_nubers()
        if len(set(numbers)) == len(numbers):
            print("Все числа уникальны")
        else:
            print("Не все числа уникальны")
        menu.Menu().menu_after_task(repeat='tasks_list.Tasks_lists().make_list_tuple().check_uniqueness()',
                                    back='self.menu_list()')
