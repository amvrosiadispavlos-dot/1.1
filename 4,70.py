k = int(input("k (1–365) = "))
day_of_week = (k - 1) % 7 + 1 
if day_of_week == 6 or day_of_week == 7:
    print("Выходной")
else:
    print("Рабочий день")
