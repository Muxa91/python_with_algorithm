class Pascals_triangle:
    height = 0

    def inputNumber(self):
        while True:
            try:
                self.height = int(input('Введите число больше нуля\n'))
                if self.height > 0:
                    break
            except ValueError:
                print('Необходимо ввести число')

    def triangle(self):
        self.inputNumber()
        row = []
        for i in range(self.height):
            row = [1] + row
            for x in range(1, len(row) - 1):
                row[x] = row[x] + row[x + 1]
            print('  ' * (self.height - len(row)), row)


t = Pascals_triangle()
t.triangle()
