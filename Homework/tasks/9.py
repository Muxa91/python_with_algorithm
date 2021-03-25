# Задача 9
# Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.

from My_project_for_Github.tasks import conversion_time


class CoversionTime(conversion_time.ConversionTime):

    def conversion(self):
        self.inputSecond()
        second = self.second
        day = second // 86400
        second = second - day * 86400

        hour = second // 3600
        second = second - hour * 3600

        minute = second // 60
        second = second - minute * 60
        print(self.cases(day, 'day'), self.cases(hour, 'hour'),\
              self.cases(minute, 'minute'), self.cases(second, 'second'))
time = CoversionTime()
time.conversion()