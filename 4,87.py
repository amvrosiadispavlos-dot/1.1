from datetime import date
y1 = int(input("Год рождения 1: "))
m1 = int(input("Месяц рождения 1: "))
d1 = int(input("День рождения 1: "))
y2 = int(input("Год рождения 2: "))
m2 = int(input("Месяц рождения 2: "))
d2 = int(input("День рождения 2: "))
birth1 = date(y1, m1, d1)
birth2 = date(y2, m2, d2)
if birth1 < birth2:
    print("Первый человек старше")
elif birth1 > birth2:
    print("Второй человек старше")
else:
    print("Одного возраста")
