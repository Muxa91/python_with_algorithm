class Arithmetic_progression:
    start = 1
    step = 1
    stop = 1

    def input_A_progr(self):
        while True:
            try:
                self.start = int(input('Введите начальное значение арифметической прогресии\n'))
                self.step = int(input('Ведите шаг арифметической прогрессии\n'))
                self.stop = int(input('Ведите конец арифметической прогрессии\n'))
                if self.start >= self.stop and self.step > 0:
                    self.step = -self.step
                    self.stop -= 1

                    break
                elif self.step == 0:
                    print("Шаг не может быть равен нулю")
                    continue
                else:
                    self.stop += 1
                    break
            except ValueError:
                print('Введите число')

    def output_range(self):
        self.input_A_progr()

        start = self.start
        stop = self.stop
        step = self.step
        for x in range(start, stop, step):
            print(x, end=' ')


Arithmetic_progression().output_range()
