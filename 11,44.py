import random
january = [random.randint(0, 15) for _ in range(31)]
total = sum(january)
print(f"Осадки за январь: {total}")
