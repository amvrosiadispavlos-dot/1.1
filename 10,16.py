import random

values = [0, 1, 2, 3, 4, 5, 6]
bone = random.sample(values, 2)
if random.choice([True, False]):
    bone = bone[::-1]  
print(f"Выбрана кость {bone[0]}-{bone[1]}")
