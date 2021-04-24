# import menu


class Arithmetic_progression():
    __start = 1
    __step = 1
    __stop = 1

    def input_A_progr(self):
        while True:
            try:
                self.__start = int(input('Введите начальное значение арифметической прогресии\n'))
                self.__step = int(input('Ведите шаг арифметической прогрессии\n'))
                self.__stop = int(input('Ведите конец арифметической прогрессии\n'))
                if self.__start >= self.__stop and self.__step > 0:
                    self.__step = -self.__step
                    self.__stop -= 1
                    break
                elif self.__step == 0:
                    print("Шаг не может быть равен нулю")
                    continue
                elif abs(self.__step) > abs(self.__stop):
                    print("Шаг не может быть больше конца арифметической")
                    continue
                else:
                    self.__stop += 1
                    break
            except ValueError:
                print('Введите число')

    def output_range(self):
        self.input_A_progr()
        start = self.__start
        stop = self.__stop
        step = self.__step
        for x in range(start, stop, step):
            print(x, end=' ')

        menu.Menu().menu_after_task(repeat='arithmetic_progression.Arithmetic_progression().output_range()',
                                    back='self.menu_mathematical_models()')
