k = int(input("k (1-365) = "))
day_of_week_a = (k - 1) % 7 + 1  
if day_of_week_a == 6:
    print("а) Суббота")
elif day_of_week_a == 7:
    print("а) Воскресенье")
else:
    print("а) Рабочий день")
d = int(input("d (1-7, 1 января) = "))
day_of_week_b = (k - 1 + d - 1) % 7 + 1
if day_of_week_b == 6:
    print("б) Суббота")
elif day_of_week_b == 7:
    print("б) Воскресенье")
else:
    print("б) Рабочий день")
