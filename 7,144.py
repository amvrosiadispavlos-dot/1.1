n = int(input("Введите количество пар n: "))
max_sum = float('-inf')
min_product = float('inf')
for i in range(n):
    a, b = map(float, input(f"Пара {i+1} (a b): ").split())
    s = a + b
    p = a * b
    if s > max_sum:
        max_sum = s
    if p < min_product:
        min_product = p
print(f"а) Максимальная сумма в паре: {max_sum}")
print(f"б) Минимальное произведение в паре: {min_product}")
