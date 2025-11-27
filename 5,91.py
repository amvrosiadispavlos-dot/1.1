n = int(input("n = "))
print("Делители:", end=" ")
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
print()
n = int(input("n = "))
total = 0
for i in range(1, n + 1):
    if n % i == 0:
        total += i
print("Сумма делителей:", total)
n = int(input("n = "))
total = 0
for i in range(2, n + 1, 2):
    if n % i == 0:
        total += i
print("Сумма чётных делителей:", total)
n = int(input("n = "))
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1
print("Количество делителей:", count)
n = int(input("n = "))
count = 0
for i in range(1, n + 1, 2):
    if n % i == 0:
        count += 1
print("Количество нечётных делителей:", count)
n = int(input("n = "))
total_count = 0
even_count = 0
for i in range(1, n + 1):
    if n % i == 0:
        total_count += 1
        if i % 2 == 0:
            even_count += 1
print("Всего делителей:", total_count)
print("Из них чётных:", even_count)
n = int(input("n = "))
d = int(input("d = "))
count = 0
for i in range(d + 1, n + 1):
    if n % i == 0:
        count += 1
print("Количество делителей >", d, ":", count)
