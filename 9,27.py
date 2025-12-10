for num in range(50, 71):
    divisors_sum = sum(i for i in range(1, num+1) if num % i == 0)
    print(f"Число {num}: сумма делителей = {divisors_sum}")
