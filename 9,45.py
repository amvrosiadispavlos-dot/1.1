m = int(input("Введите m: "))
n = int(input("Введите n: "))
for num in range(1, n):
    digits_sum = sum(int(d) for d in str(num))
    if digits_sum**2 == m:
        print(num)
