s = int(input("s (1-27) = "))
count = 0
for num in range(100, 1000):
    digit_sum = num // 100 + (num // 10) % 10 + num % 10
    if digit_sum == s:
        count += 1
print("Количество чисел:", count)
