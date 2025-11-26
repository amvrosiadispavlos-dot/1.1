n = int(input("n (1-1188 месяцев) = "))
years = n // 12
months = n % 12
if 11 <= years <= 19:
    years_word = "лет"
else:
    last_y = years % 10
    if last_y == 1:
        years_word = "год"
    elif 2 <= last_y <= 4:
        years_word = "года"
    else:
        years_word = "лет"
if 11 <= months <= 19:
    months_word = "месяцев"
else:
    last_m = months % 10
    if last_m == 1:
        months_word = "месяц"
    elif 2 <= last_m <= 4:
        months_word = "месяца"
    else:
        months_word = "месяцев"
if years == 0:
    print(f"{months} {months_word}")
elif months == 0:
    print(f"{years} {years_word} ровно")
else:
    print(f"{years} {years_word} {months} {months_word}")
