import main

class Tasks_string:
    def input_string(self):
        while True:
            try:
                string = input('Введите предложение\n')
                break
            except:
                string = input('Введите предложение\n')
        return string

    # Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное.
    def find_long_and_frequent(self):
        print('Программа, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное.')
        string = self.input_string()
        string = string.split(' ')
        longword = max(string, key=len)
        def counter(string):
            count = 0
            dict = {}
            for x in string:
                for j in string:
                    if x == j:
                        count += 1
                dict[count] = x
                count = 0
            return dict[max(dict)]

        print('Самое длинное слово: ', longword, '.Самое часто встречаемое слова: ', counter(string))

        main.Menu().menu_after_task(repeat='task_strings.Tasks_string().find_long_and_frequent()',
                                back='self.menu_string()')

    # Посчитайте, сколько раз символ встречается в строке
    def find_symbol(self):
        string = self.input_string()
        symbol = input('Введите символ')
        count = 0
        for x in string:
            if x == symbol:
                count += 1
        main.Menu().menu_after_task(repeat='task_strings.Tasks_string().find_symbol()',
                                back='self.menu_string()')

    # Найти палиндром
    def find_palindrome(self):
        string = self.input_string()
        string = string.split(' ')
        tmp = ''
        for word in string:
            if word == tmp.join(reversed(word)):
                print(word, 'Палиндром', end='\t')
            else:
                print(word, 'Не алиндром', end='\t')
        main.Menu().menu_after_task(repeat='task_strings.Tasks_string().find_palindrome()',
                                back='self.menu_string()')