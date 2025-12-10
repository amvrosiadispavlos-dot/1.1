n = 1
while True:
    value = 1 + 1.0 / n if n > 1 else 1.0
    if value > n:
        print(f"Первое число 1 + 1/n > n: при n = {n}, значение = {value:.3f}")
        break
    n += 1
