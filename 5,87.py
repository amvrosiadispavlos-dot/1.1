count = 0
for num in range(100, 501):
    digit_sum = sum(int(d) for d in str(num))
    if digit_sum == 15:
        count += 1
print("Количество чисел:", count)
