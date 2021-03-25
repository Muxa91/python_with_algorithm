class Tetration:
    number = 0
    tetrator = 0

    def inputNumber(self):
        while True:
            try:
                self.number = int(input('Введите число больше нуля или ранвное "-1"\n'))
                if self.number > 0 or self.number == -1:
                    while True:
                        self.tetrator = int(input('Введите Тетратор больше или равный нулю\n'))
                        if self.tetrator >= 0:
                            break
                    break
            except ValueError:
                print('Необходимо ввести число')

    def tetration(self):
        self.inputNumber()
        counter = 0
        result = self.number
        while counter < self.tetrator*2:
            result = result ** self.number
            counter += 1
        print('Тетратор равен', result)


t = Tetration()
t.tetration()
