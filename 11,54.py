import random
books_per_section = [random.randint(100, 5000) for _ in range(35)]
total_books = sum(books_per_section)
print(f"Общее число книг: {total_books}")
print(f"Шестизначное число: {100000 <= total_books <= 999999}")
