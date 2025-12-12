import random
september = [random.randint(0, 25) for _ in range(30)]
decade1 = september[:10]
decade2 = september[10:20]
decade3 = september[20:]
avg1 = sum(decade1) / len(decade1)
avg2 = sum(decade2) / len(decade2)
avg3 = sum(decade3) / len(decade3)
print(f"Среднее за 1-ю декаду: {avg1:.2f}")
print(f"Среднее за 2-ю декаду: {avg2:.2f}")
print(f"Среднее за 3-ю декаду: {avg3:.2f}")
