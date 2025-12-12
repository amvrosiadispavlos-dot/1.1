arr = list(range(1, 21))
print("Исходный массив:", arr)
first_three = arr[:3]
last_three = arr[-3:]
arr[:3] = last_three
arr[-3:] = first_three
print("После перестановки первых и последних трех:", arr)
