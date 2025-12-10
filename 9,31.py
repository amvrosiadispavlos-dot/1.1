num = 1
while num < 100000:
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    if divisors_sum == num:
        print(num)
    num += 1
