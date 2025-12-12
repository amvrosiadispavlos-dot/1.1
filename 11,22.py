arr = [5, -3, 10, 150, -20, 80, 99]
print("а) Неотрицательные элементы:")
print([x for x in arr if x >= 0])
print("б) Элементы, не превышающие 100:")
print([x for x in arr if x <= 100])
