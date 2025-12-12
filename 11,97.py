import random
heights = [random.randint(150, 190) for _ in range(25)]
avg_height = sum(heights) / len(heights)
count = sum(1 for h in heights if h > avg_height)
print(f"Средний рост: {avg_height:.1f}")
print(f"Количество учеников выше среднего: {count}")
