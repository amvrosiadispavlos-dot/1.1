import random
results = [random.uniform(9.5, 12.0) for _ in range(22)]
sorted_results = sorted(results)
first_second = sorted_results[:2]
print(f"Результаты первого и второго мест: {first_second}")
