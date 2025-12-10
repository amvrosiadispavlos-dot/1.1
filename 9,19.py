for num in range(120, 141):
    divisors = [i for i in range(1, num+1) if num % i == 0]
    print(f"Число {num}: {len(divisors)} делителей")
