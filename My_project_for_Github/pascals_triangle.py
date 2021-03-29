import menu
class Pascals_triangle:
    __height = 0

    def inputNumber(self):
        while True:
            try:
                self.__height = int(input('Введите число больше нуля\n'))
                if self.__height > 0:
                    break
            except ValueError:
                print('Необходимо ввести число')

    def triangle(self):
        self.inputNumber()
        row = []
        for i in range(self.__height):
            row = [1] + row
            for x in range(1, len(row) - 1):
                row[x] = row[x] + row[x + 1]
            print('  ' * (self.__height - len(row)), row)

        menu.Menu().menu_after_task(repeat='pascals_triangle.Pascals_triangle().triangle()',
                                    back='self.menu_mathematical_models()')
