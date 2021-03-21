class ConversionCurrency:
    money = 112
    smallСhange = 0
    currency_input = '2'
    currency_output = '1'
    currency = {1: 'Доллар', 2: "Евро", 3: "Лира"}
    currency_small_change = {1: 'Цент', 2: 'Евро-цент', 3: 'Куруш'}
    # Костыль в методе(converter)выдает ошибку "KeyError"
    currencyText = currency[int(currency_output)]
    small_change_text = currency_small_change[int(currency_output)]

    def inputCurrency(self):
        currency_tmp = self.currency
        # Choosing a currency to convert
        while True:
            try:
                print("Выберете валюту для конвертации\n", currency_tmp)
                self.currency_input = int(input(''))
                if 0 >= self.currency_input >= 4:
                    print("Выберете валюту для конвертации\n", currency_tmp)
                    self.currency_input = int(input(''))

                else:
                    if self.currency_input == 1:
                        self.money = int(input('Сколько Долларов необходимо конвертировать?\n'))
                        self.smallСhange = int(input('Сколько центов необходимо конвертировать?\n'))
                        while self.smallСhange > 99:
                            self.smallСhange = int(input('Введите число меньше ста\n'))
                    if self.currency_input == 2:
                        self.money = int(input('Сколько Евро необходимо конвертировать?\n'))
                        self.smallСhange = int(input('Сколько евро-центов необходимо конвертировать?\n'))
                        while self.smallСhange > 99:
                            self.smallСhange = int(input('Введите число меньше ста\n'))
                    if self.currency_input == 3:
                        self.money = int(input('Сколько Лир необходимо конвертировать?\n'))
                        self.smallСhange = int(input('Сколько курушей необходимо конвертировать?\n'))
                        while self.smallСhange > 99:
                            self.smallСhange = int(input('Введите число меньше ста\n'))
                    currency_tmp.pop(self.currency_input)
                    break
            except ValueError:
                print("Необходимо ввести число")

        # Choosing which currency to convert
        while True:
            try:
                print("В какую валюту вы хотите конвертировать? \n", currency_tmp)
                self.currency_output = int(input(''))
                self.currencyText = self.currency[int(self.currency_output)]
                self.small_change_text = self.currency_small_change[int(self.currency_output)]
                if 0 >= self.currency_output >= 4:
                    print("В какую валюту вы хотите конвертировать? \n", currency_tmp)
                    self.currency_output = int(input(''))
                else:
                    currency_tmp.pop(self.currency_output)
                    break
            except ValueError:
                print("Необходимо ввести число")

    # word conjugation
    def casesCurency(self, currency, money):
        currency = currency
        money = money

        if 11 <= int(str(money)[-2:]) <= 19:
            if currency == "Доллар":
                return str(money) + " Долларов"
            if currency == "Лира":
                return str(money) + " Лир"
            if currency == "Цент":
                return str(money) + ' Центов'
            if currency == "Евро-цент":
                return str(money) + ' Евро-центов'
            if currency == "Куруш":
                return str(money) + ' Курушей'
        elif str(money)[-1] == '1':
            if currency == "Доллар":
                return str(money) + " Доллар"
            if currency == "Лира":
                return str(money) + " Лира"
            if currency == "Цент":
                return str(money) + 'Цент'
            if currency == "Евро-цент":
                return str(money) + ' Евро-цент'
            if currency == "Куруш":
                return str(money) + ' Куруш'
        elif 2 <= int(str(money)[-1]) <= 4:
            if currency == "Доллар":
                return str(money) + " Доллара"
            if currency == "Лира":
                return str(money) + " Лиры"
            if currency == "Цент":
                return str(money) + ' Цента'
            if currency == "Евро-цент":
                return str(money) + ' Евро-цента'
            if currency == "Куруш":
                return str(money) + ' Куруша'
        else:
            if currency == "Доллар":
                return str(money) + " Долларов"
            if currency == "Лира":
                return str(money) + " Лир"
            if currency == "Цент":
                return str(money) + ' Центов'
            if currency == "Евро-цент":
                return str(money) + ' Евро-центов'
            if currency == "Куруш":
                return str(money) + ' Курушей'

    def converter(self):
        self.inputCurrency()
        # currency {1-USD,2-EUR, 3-LIR}
        ratio = {1: 1, 2: 0.84, 3: 7.22}

        resultCurrency = int(
            (self.money + self.smallСhange / 100) * ratio[self.currency_output] // ratio[self.currency_input])
        currency_small_change = int(
            ((self.money + self.smallСhange / 100) * ratio[self.currency_output] / ratio[
                self.currency_input] - resultCurrency) * 100)

        print(self.currency_output)
        print(self.currencyText)
        print(self.casesCurency(currency=self.currencyText, money=resultCurrency),
              self.casesCurency(currency=self.small_change_text, money=currency_small_change))


c = ConversionCurrency()
c.converter()
