arr = [12, 15, 24, 35, 40, 55, 62]
even_count = sum(1 for x in arr if x % 2 == 0)
ends_with_5 = sum(1 for x in arr if x % 10 == 5)
print(f"Четных: {even_count}")
print(f"Оканчивающихся на 5: {ends_with_5}")
