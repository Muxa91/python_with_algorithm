import main
class Tetration:
    __number = 0
    __tetrator = 0

    def inputNumber(self):
        while True:
            try:
                self.__number = int(input('Введите число больше нуля или ранвное "-1"\n'))
                if self.__number > 0 or self.__number == -1:
                    while True:
                        self.__tetrator = int(input('Введите Тетратор больше или равный нулю\n'))
                        if self.__tetrator >= 0:
                            break
                    break
            except ValueError:
                print('Необходимо ввести число')

    def tetration(self):
        self.inputNumber()
        counter = 0
        result = self.__number
        while counter < self.__tetrator*2:
            result = result ** self.__number
            counter += 1
        print('Тетратор равен', result)

        main.Menu().menu_after_task(repeat='tetration.Tetration().tetration()',
                                back='self.menu_mathematical_models()')

