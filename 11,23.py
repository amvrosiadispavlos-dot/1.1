arr = [12, 7, 20, 33, 40, 55, 60]
print("а) Четные элементы:")
print([x for x in arr if x % 2 == 0])
print("б) Элементы, оканчивающиеся нулем:")
print([x for x in arr if x % 10 == 0])
