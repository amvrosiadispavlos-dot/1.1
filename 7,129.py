print("Введите последовательность целых чисел, оканчивающуюся -1:")
seq = []
while True:
    num = int(input())
    if num == -1:
        break
    seq.append(num)
index_mult7 = -1
for i in range(len(seq)):
    if seq[i] % 7 == 0:
        index_mult7 = i + 1
        break
if index_mult7 != -1:
    print(f"Первое число, кратное 7, на позиции {index_mult7}")
else:
    print("Нет чисел, кратных 7")
