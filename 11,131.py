import random
weights = [random.randint(50, 120) for _ in range(20)]
max_weight = max(weights)
min_weight = min(weights)
condition = max_weight > 2 * min_weight
print(f"Вес самого тяжелого превышает вес самого легкого более чем в 2 раза: {condition}")
