currency = "Доллар"
money = 1312
govno =str(money)[-1]
print(int(str(money)[-2:]))
if 11 <= int(str(money)[-2:]) <= 19:
    if currency == "Доллар":
        print(str(money) + " Долларов")
    if currency == "Лира":
        print(str(money) + " Лир")
elif govno == '1':
    if currency == "Доллар":
        print(str(money) + " Доллар")
    if currency == "Лира":
        print(str(money) + " Лира")
elif 2<= int(govno) <= 4 :
    if currency == "Доллар":
        print(str(money) + " Доллара")
    if currency == "Лира":
        print(str(money) + " Лиры")
else:
    if currency == "Доллар":
        print(str(money) + " Долларов")
    if currency == "Лира":
        print(str(money) + " Лир")