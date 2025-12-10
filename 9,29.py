for num in range(300, 601):
    divisors_sum = sum(i for i in range(1, num+1) if num % i == 0)
    if divisors_sum % 10 == 0:
        print(num)
