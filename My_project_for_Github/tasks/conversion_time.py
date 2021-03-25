class ConversionTime:
    second = 60

    def inputSecond(self):
        while True:
            try:
                self.second = int(input('Введите количество секунд\n'))
                if self.second <= 0:
                    self.second = int(input('Введите положительное число\n'))
                else:
                    break
            except ValueError:
                print("Необходимо ввести число\n")

    def cases(self, time_unit, time_unit_text):
        time_unit = time_unit
        time_unit_text = time_unit_text
        # Числа с 11 по 19
        if 11 <= int(str(time_unit)[-2:]) <= 19:
            if time_unit_text == 'year':
                return str(time_unit) + " Лет"
            if time_unit_text == "month":
                return str(time_unit) + " Месяцев"
            if time_unit_text == "week":
                return str(time_unit) + ' Недель'
            if time_unit_text == "day":
                return str(time_unit) + ' Дней'
            if time_unit_text == "hour":
                return str(time_unit) + ' Часов'
            if time_unit_text == "minute":
                return str(time_unit) + ' Минут'
            if time_unit_text == "second":
                return str(time_unit) + ' Секунд'
        # первое число
        elif str(time_unit)[-1] == '1':
            if time_unit_text == 'year':
                return str(time_unit) + " Год"
            if time_unit_text == "month":
                return str(time_unit) + " Месяц"
            if time_unit_text == "week":
                return str(time_unit) + ' Неделя'
            if time_unit_text == "day":
                return str(time_unit) + ' День'
            if time_unit_text == "hour":
                return str(time_unit) + ' Час'
            if time_unit_text == "minute":
                return str(time_unit) + ' Минута'
            if time_unit_text == "second":
                return str(time_unit) + ' Секунда'
        # числа оканчивающиеся с 2 по 4
        elif 2 <= int(str(time_unit)[-1]) <= 4:
            if time_unit_text == 'year':
                return str(time_unit) + " Года"
            if time_unit_text == "month":
                return str(time_unit) + " Месяца"
            if time_unit_text == "week":
                return str(time_unit) + ' Недели'
            if time_unit_text == "day":
                return str(time_unit) + ' Дня'
            if time_unit_text == "hour":
                return str(time_unit) + ' Часа'
            if time_unit_text == "minute":
                return str(time_unit) + ' Минуты'
            if time_unit_text == "second":
                return str(time_unit) + ' Секунды'
        # Числа оканчивающиеся с 5 по 9
        else:
            if time_unit_text == 'year':
                return str(time_unit) + " Лет"
            if time_unit_text == "month":
                return str(time_unit) + " Месяцев"
            if time_unit_text == "week":
                return str(time_unit) + ' Недель'
            if time_unit_text == "day":
                return str(time_unit) + ' Дней'
            if time_unit_text == "hour":
                return str(time_unit) + ' Часов'
            if time_unit_text == "minute":
                return str(time_unit) + ' Минут'
            if time_unit_text == "second":
                return str(time_unit) + ' Секунд'

    def conversion(self):
        self.inputSecond()
        second = self.second

        year = second // 31536000
        second = second - year * 31536000

        month = second // 2678400
        second = second - month * 2678400

        week = second // 604800
        second = second - week * 604800

        day = second // 86400
        second = second - day * 86400

        hour = second // 3600
        second = second - hour * 3600

        minute = second // 60
        second = second - minute * 60
        
        print(self.cases(year, 'year'), self.cases(month, 'month'), self.cases(week, 'week'), self.cases(day, 'day'),\
              self.cases(hour, 'hour'), self.cases(minute, 'minute'), self.cases(second, 'second'))

t = ConversionTime()
t.conversion()
