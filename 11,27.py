arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = [x for x in arr if x % 2 == 0]
odd = [x for x in arr if x % 2 != 0]
print("Четные элементы:", even)
print("Нечетные элементы:", odd)
