# Сложите цифры целого числа.
def sum_number(number):
    number=sum([int(x) for x in str(number)])
    print(number)
sum_number(234)