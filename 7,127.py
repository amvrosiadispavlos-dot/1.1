print("Введите последовательность целых чисел, оканчивающуюся 100:")
seq = []
while True:
    num = int(input())
    if num == 100:
        break
    seq.append(num)
index_666 = -1
for i in range(len(seq)):
    if seq[i] == 666:
        index_666 = i + 1
        break
if index_666 != -1:
    print(f"Число 666 найдено на позиции {index_666}")
else:
    print("Числа 666 нет в последовательности")
