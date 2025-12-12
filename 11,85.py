import random
heights = [random.randint(155, 195) for _ in range(30)]
tall_count = sum(1 for h in heights if h > 170)
print(f"Учеников выше 170 см: {tall_count}")
print(f"Можно сформировать команду (≥5): {tall_count >= 5}")
