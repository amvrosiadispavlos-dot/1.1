print("Введите последовательность целых чисел, оканчивающуюся нулём:")
seq = []
while True:
    num = int(input())
    if num == 0:
        break
    seq.append(num)
print("Сумма:", sum(seq))
print("Количество:", len(seq))
