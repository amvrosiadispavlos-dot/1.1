import random
heights = [random.randint(160, 200) for _ in range(35)]
max_height = max(heights)
count = heights.count(max_height)
print(f"Количество человек с максимальным ростом ({max_height} см): {count}")
