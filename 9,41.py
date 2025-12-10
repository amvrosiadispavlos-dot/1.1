n = int(input("Введите n (n ≤ 27): "))
for d1 in range(10):
    for d2 in range(10):
        for d3 in range(10):
            if d1 + d2 + d3 == n and d1 != 0:
                print(d1*100 + d2*10 + d3)
