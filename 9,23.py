a = int(input("Введите a: "))
b = int(input("Введите b: "))
k = int(input("Введите k: "))
for num in range(a, b+1):
    divisors = [i for i in range(1, num+1) if num % i == 0]
    if len(divisors) == k:
        print(num)
