import random
pages = [random.randint(100, 500) for _ in range(100)]
max_pages = max(pages)
print(f"Количество страниц в самой толстой книге: {max_pages}")
