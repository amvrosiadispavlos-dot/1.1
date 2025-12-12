import random
class_sizes = [random.randint(20, 35) for _ in range(40)]
max_class = max(class_sizes)
min_class = min(class_sizes)
condition = (max_class - min_class) == 10
print(f"В самом многочисленном классе на 10 учеников больше, чем в самом малочисленном: {condition}")
