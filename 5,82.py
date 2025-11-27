for num in range(10, 100):
    d1, d2 = num // 10, num % 10
    if (d1**2 + d2**2) % 13 == 0:
        print(num, end=" ")
print()
for num in range(10, 100):
    digit_sum = num // 10 + num % 10
    if digit_sum + digit_sum ** 2 == num:
        print(num, end=" ")
print()
