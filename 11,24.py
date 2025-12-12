arr = [5, 23, 456, 78, 1234, 99, 7, 100, 789]
print("а) Двузначные числа:")
print([x for x in arr if 10 <= x <= 99])
print("б) Трехзначные числа:")
print([x for x in arr if 100 <= x <= 999])
