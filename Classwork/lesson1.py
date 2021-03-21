# # for i in range(1, 20, 5):
# #
#
#
# number=int(input('введите число '))
# # factorial = 1
# # for i in range(1, number+1):
# #     factorial *= i
# # #
# # # print(factorial)
# # #
# # print(range(1, 10))
# for i in range(1, 10):
#
#     for g in range(1, 10):
#         print(g*i, end='\t')
#     print('\n')
#
while True:
    try:
        number = int(input('Введите число '))
        number2 = int(input('Введите число 2 '))
        number3 = number / number2
        print('Введенное число', number3)

    except ValueError as e:
        print('преоброзавание прошло неудачно', e)
    except:

        print("ошибка")
    finally:
        print('Это блок файноли будет выполняться всегда')

