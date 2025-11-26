day = int(input("Номер дня недели (1-7) = "))
if day == 1:
    name = "понедельник"
elif day == 2:
    name = "вторник"
elif day == 3:
    name = "среда"
elif day == 4:
    name = "четверг"
elif day == 5:
    name = "пятница"
elif day == 6:
    name = "суббота"
elif day == 7:
    name = "воскресенье"
else:
    name = "неверный номер"
print("День недели:", name)
