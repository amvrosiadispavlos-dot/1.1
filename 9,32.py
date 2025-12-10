a = int(input("Введите a: "))
b = int(input("Введите b: "))
max_sum = 0
result_num = a
for num in range(a, b+1):
    divisors_sum = sum(i for i in range(1, num+1) if num % i == 0)
    if divisors_sum > max_sum:
        max_sum = divisors_sum
        result_num = num
print(f"Число {result_num} имеет максимальную сумму делителей = {max_sum}")
11
