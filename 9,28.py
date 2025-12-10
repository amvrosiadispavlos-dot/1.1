for num in range(100, 301):
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    if divisors_sum == 50:
        print(num)

