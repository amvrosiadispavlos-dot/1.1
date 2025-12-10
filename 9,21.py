for num in range(1, 301):
    divisors = [i for i in range(1, num+1) if num % i == 0]
    if len(divisors) == 5:
        print(num)
