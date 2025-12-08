print("Введите последовательность положительных чисел, оканчивающуюся нулём:")
while True:
    num = int(input())
    if num == 0:
        break
    print(num, end=' ')
