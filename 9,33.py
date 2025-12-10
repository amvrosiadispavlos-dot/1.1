def sum_of_divisors(n):
    return sum(i for i in range(1, n) if n % i == 0)
for a in range(1, 50000):
    b = sum_of_divisors(a)
    if b > a and b < 50000:
        if sum_of_divisors(b) == a:
            print(f"Дружественные числа: {a} и {b}")
