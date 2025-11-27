for num in range(100, 1000):
    if (num ** 2) % 1000 == num:
        print(num, end=" ")
print()
for num in range(100, 1000):
    if num % 7 == 0:
        digit_sum = num // 100 + (num // 10) % 10 + num % 10
        if digit_sum % 7 == 0:
            print(num, end=" ")
print()
