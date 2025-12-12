import random
heights = [random.randint(155, 195) for _ in range(25)]
max_height = max(heights)
min_height = min(heights)
difference = max_height - min_height
print(f"Рост самого высокого: {max_height} см")
print(f"Рост самого низкого: {min_height} см")
print(f"Разница: {difference} см")
