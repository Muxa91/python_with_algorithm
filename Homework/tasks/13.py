
# Задача 13
# При заданном целом числе n посчитайте n + nn + nnn.

def expression_nuber(number):
    number=number+number*2+number*3
    print(number)
    
expression_nuber(5)