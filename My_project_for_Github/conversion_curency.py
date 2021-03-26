import main
class ConversionCurrency:
    __money = 112
    __smallСhange = 0
    __currency_input = '2'
    __currency_output = '1'
    __currency = {1: 'Доллар', 2: "Евро", 3: "Лира"}
    __currency_small_change = {1: 'Цент', 2: 'Евро-цент', 3: 'Куруш'}
    __currencyText = __currency[int(__currency_output)]
    __small_change_text = __currency_small_change[int(__currency_output)]

    def inputCurrency(self):
        currency_tmp = self.__currency
        # Choosing a currency to convert
        while True:
            try:
                print("Выберете валюту для конвертации\n", currency_tmp)
                self.__currency_input = int(input(''))
                if 0 >= self.__currency_input >= 4:
                    print("Выберете валюту для конвертации\n", currency_tmp)
                    self.__currency_input = int(input(''))

                else:
                    if self.__currency_input == 1:
                        self.__money = int(input('Сколько Долларов необходимо конвертировать?\n'))
                        self.__smallСhange = int(input('Сколько центов необходимо конвертировать?\n'))
                        while self.__smallСhange > 99:
                            self.__smallСhange = int(input('Введите число меньше ста\n'))
                    if self.__currency_input == 2:
                        self.__money = int(input('Сколько Евро необходимо конвертировать?\n'))
                        self.__smallСhange = int(input('Сколько евро-центов необходимо конвертировать?\n'))
                        while self.__smallСhange > 99:
                            self.__smallСhange = int(input('Введите число меньше ста\n'))
                    if self.__currency_input == 3:
                        self.__money = int(input('Сколько Лир необходимо конвертировать?\n'))
                        self.__smallСhange = int(input('Сколько курушей необходимо конвертировать?\n'))
                        while self.__smallСhange > 99:
                            self.__smallСhange = int(input('Введите число меньше ста\n'))
                    currency_tmp.pop(self.__currency_input)
                    break
            except ValueError:
                print("Необходимо ввести число")

        # Choosing which currency to convert
        while True:
            try:
                print("В какую валюту вы хотите конвертировать? \n", currency_tmp)
                self.__currency_output = int(input(''))
                self.__currencyText = self.__currency[int(self.__currency_output)]
                self.__small_change_text = self.__currency_small_change[int(self.__currency_output)]
                if 0 >= self.__currency_output >= 4:
                    print("В какую валюту вы хотите конвертировать? \n", currency_tmp)
                    self.__currency_output = int(input(''))
                else:
                    currency_tmp.pop(self.__currency_output)
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
            (self.__money + self.__smallСhange / 100) * ratio[self.__currency_output] // ratio[self.__currency_input])
        currency_small_change = int(
            ((self.__money + self.__smallСhange / 100) * ratio[self.__currency_output] / ratio[
                self.__currency_input] - resultCurrency) * 100)

        print(self.__currency_output)
        print(self.__currencyText)
        print(self.casesCurency(currency=self.__currencyText, money=resultCurrency),
              self.casesCurency(currency=self.__small_change_text, money=currency_small_change))

        main.Menu().menu_after_task(repeat='conversion_curency.ConversionCurrency().converter()',
                                    back='self.menu_mathematical_models()')



