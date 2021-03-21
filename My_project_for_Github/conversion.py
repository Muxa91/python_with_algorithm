
class ConversionCurrency:
    money = 112
    currency_input = '2'
    currency_output = '1'
    currency = {1: 'Доллар', 2: "Евро", 3: "Лира"}
    # Костыль в методе(converter)выдает ошибку "KeyError"
    currencyText =currency[int(currency_output)]
    def inputCurrency(self):
        currency_tmp = self.currency
        # Choosing a currency to convert
        while True:
            try:
                self.money = int(input('Сколько денег необходимо конвертировать?\n'))
                print("Выберете валюту для конвертации\n", currency_tmp)
                self.currency_input = int(input(''))
                if 0 >= self.currency_input >= 4:
                    print("Выберете валюту для конвертации\n", currency_tmp)
                    self.currency_input = int(input(''))

                else:
                    currency_tmp.pop(self.currency_input)
                    break
            except ValueError:
                print("Необходимо ввести число")

        # Choosing which currency to convert
        while True:
            try:
                print("В какую валюты вы хотите конвертировать? \n", currency_tmp)
                self.currency_output = int(input(''))
                if 0 >= self.currency_output >= 4:
                    print("В какую валюты вы хотите конвертировать? \n", currency_tmp)
                    self.currency_output = int(input(''))
                else:
                    currency_tmp.pop(self.currency_output)
                    break
            except ValueError:
                print("Необходимо ввести число")

    def casesCurency(self, currency, money):
        currency = currency
        money = money
        if 11 <= int(str(money)[-2:]) <= 19:
            if currency == "Доллар":
                return str(money) + " Долларов"
            if currency == "Лира":
                return str(money) + " Лир"
        elif str(money)[-1] == '1':
            if currency == "Доллар":
                return str(money) + " Доллар"
            if currency == "Лира":
                return str(money) + " Лира"
        elif 2 <= int(str(money)[-1]) <= 4:
            if currency == "Доллар":
                return str(money) + " Доллара"
            if currency == "Лира":
                return str(money) + " Лиры"
        else:
            if currency == "Доллар":
                return str(money) + " Долларов"
            if currency == "Лира":
                return str(money) + " Лир"
    def converter (self):
        self.inputCurrency()
        # currency {1-USD,2-EUR, 3-LIR}
        ratio = {1: 1, 2: 0.84, 3: 7.22}

        resultCurrency = int(self.money*ratio[self.currency_output]//ratio[self.currency_input])
        smallСhange = int((self.money*ratio[self.currency_output]/ratio[self.currency_input]-resultCurrency)*100)
        print(self.casesCurency(currency=self.currencyText, money=self.money))
c = ConversionCurrency()
c.converter()
