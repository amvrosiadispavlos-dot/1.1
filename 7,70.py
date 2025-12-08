print("Введите количество осадков за каждый день мая (31 число через пробел):")
precip = list(map(float, input().split()[:31]))
count_no_precip = 0
for p in precip:
    if p == 0:
        count_no_precip += 1
    else:
        break  
print(f"Количество первых дней без осадков (случай 1): {count_no_precip}")
print("Введите количество осадков за каждый день мая (31 число через пробел):")
precip = list(map(float, input().split()[:31]))
count_no_precip = 0
for p in precip:
    if p == 0:
        count_no_precip += 1
    else:
        break
print(f"Количество первых дней без осадков (случай 2): {count_no_precip}")
