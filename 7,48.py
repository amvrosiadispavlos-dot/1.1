print("Введите количество страниц в газетах и журналах через пробел (закончите ввод любым нечисловым символом):")
pages = []
while True:
    try:
        p = int(input())
        pages.append(p)
    except:
        break
    16 страниц, журнал > 16
total_journal_pages = sum(p for p in pages if p > 16)
print(f"Общее число страниц во всех журналах: {total_journal_pages}")
