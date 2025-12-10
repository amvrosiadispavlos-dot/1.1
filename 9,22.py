for num in range(200, 501):
    divisors = [i for i in range(1, num+1) if num % i == 0]
    if len(divisors) == 6:
        print(num)
