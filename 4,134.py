month = int(input("Номер месяца (1-12) = "))
if month == 1:
    name = "январь"
elif month == 2:
    name = "февраль"
elif month == 3:
    name = "март"
elif month == 4:
    name = "апрель"
elif month == 5:
    name = "май"
elif month == 6:
    name = "июнь"
elif month == 7:
    name = "июль"
elif month == 8:
    name = "август"
elif month == 9:
    name = "сентябрь"
elif month == 10:
    name = "октябрь"
elif month == 11:
    name = "ноябрь"
elif month == 12:
    name = "декабрь"
else:
    name = "неверный номер"
print("Месяц:", name)
