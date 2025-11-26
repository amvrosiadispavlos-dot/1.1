n = int(input("n (1-9999 копеек) = "))
rub = n // 100
kop = n % 100
if 11 <= rub <= 19:
    rub_word = "рублей"
else:
    last_rub = rub % 10
    if last_rub == 1:
        rub_word = "рубль"
    elif 2 <= last_rub <= 4:
        rub_word = "рубля"
    else:
        rub_word = "рублей"
if 11 <= kop <= 19:
    kop_word = "копеек"
else:
    last_kop = kop % 10
    if last_kop == 1:
        kop_word = "копейка"
    elif 2 <= last_kop <= 4:
        kop_word = "копейки"
    else:
        kop_word = "копеек"
if rub == 0:
    print(f"{kop} {kop_word}")
elif kop == 0:
    print(f"{rub} {rub_word} ровно")
else:
    print(f"{rub} {rub_word} {kop} {kop_word}")
