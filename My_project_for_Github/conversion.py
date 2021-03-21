
class ConversionCurrency:
    currency_input = ''
    currency_output = ''

    def inputCurrency(self):
        # Choosing a currency to convert
        while True:
            try:
                self.currency_input = int(input('Выберете валюту для конвертации: \n 1 Доллар \n 2 Евро\n 3 Лира \n'))
                if 0 >= self.currency_input <= 4:
                    continue
                else:
                    if self.currency_input == 1:
                        print('Вы выбрали Доллар')
                    elif self.currency_input ==2:
                        print('Вы выбрали Евро')
                    else:
                        print('Вы выбрали лиру')
                    break
            except ValueError:
                print('Выберете валюту для конвертации: \n 1 Доллар \n 2 Евро\n 3 Лира \n')

        # Choosing which currency to convert
        while True:
            try:
                if self.currency_input == 1:
                    self.currency_output = int(input('В какю валюты вы хотите конвертировать?\n 2 Евро\n 3 Лира \n'))
                elif self.currency_input == 2:
                    self.currency_output = int(input('В какю валюты вы хотите конвертировать?\n 1 Доллар\n 3 Лира \n'))
                elif self.currency_input == 3:
                    self.currency_output = int(input('В какю валюты вы хотите конвертировать?\n 1 Доллар\n 2 Евро \n'))
                elif 0 >= self.currency_output <= 4:
                    continue
                else:
                    if self.currency_output == 1:
                        print('Вы выбрали Доллар')
                    elif self.currency_output ==2:
                        print('Вы выбрали Евро')
                    else:
                        print('Вы выбрали лиру')
                    break
            except ValueError:
                continue
c = ConversionCurrency()
c.inputCurrency()