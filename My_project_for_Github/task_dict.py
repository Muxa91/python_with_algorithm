import menu


class Tasks_dict:
    __my_dict = {}
    __my_dict2 = {}



    def __input_dict(self):

        while True:
            try:
                my_dict = self.__my_dict
                print('введите ключ словаря.Нажмите enter для продолжения\n')
                key = input()
                if key == '':
                    break
                print('введите значение\n')
                value = input()
                my_dict[key] = value
            except:
                print('')
        return my_dict

    # Отсортируйте словарь по значению в порядке возрастания и убывания.
    def sort_dict(self):
        print('Сортировка словаря по значению в порядке возрастания и убывания.')
        self.__input_dict()
        # по возрастанию
        my_dict = self.__my_dict
        sortedKey = sorted(my_dict, key=my_dict.get)
        my_dict_sorted = {}
        my_dict_sorted_reverse ={}
        for x in sortedKey:
            my_dict_sorted[x] = my_dict[x]
        # по убыванию
        sortedKey.reverse()
        for x in sortedKey:
            my_dict_sorted_reverse[x] = my_dict[x]
        print(my_dict_sorted)
        print(my_dict_sorted_reverse)
        menu.Menu().menu_after_task(repeat='task_dict.Tasks_dict().sort_dict()',
                                back='self.menu_dict()')

    # Напишите программу для слияния нескольких словарей в один.
    def merger_two_dict(self):
        print('Напиcать программу для слияния нескольких словарей в один.\n Введите первый словарь')
        self.__my_dict = self.__input_dict()

        print('Введите второй словарь')
        self.__my_dict2 = self.__input_dict()
        result = {**self.__my_dict, **self.__my_dict2}
        print(result)
        menu.Menu().menu_after_task(repeat='task_dict.Tasks_dict().merger_two_dict()',
                                back='self.menu_dict()')

    # Найдите три ключа с самыми высокими значениями в словаре

    def find_three_max_values(self):
        print('Найти три ключа с самыми высокими значениями в словаре')
        self.__my_dict = self.__input_dict()
        sortedKey = sorted(self.__my_dict, key=self.__my_dict.get)
        sortedKey.reverse()
        sortedKey = sortedKey[:3]
        my_dict_sorted = {}
        for x in sortedKey:
            my_dict_sorted[x] = self.__my_dict[x]
        print(my_dict_sorted)
        menu.Menu().menu_after_task(repeat='task_dict.Tasks_dict().find_three_max_values()',
                                back='self.menu_dict()')