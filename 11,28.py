arr = [10, 25, 30, 47, 50, 63, 70]
indices = [i for i, x in enumerate(arr) if x % 10 == 0]
print("Номера элементов, оканчивающихся на 0:", indices)
