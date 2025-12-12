import random
arr = sorted([random.randint(1, 20) for _ in range(30)])
print("Массив (неубывающий):", arr)
unique_count = len(set(arr))
print(f"Количество различных чисел: {unique_count}")
