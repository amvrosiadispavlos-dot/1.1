print("Введите неубывающую последовательность вещественных чисел, оканчивающуюся 1000:")
seq = []
while True:
    num = float(input())
    if num == 1000:
        break
    seq.append(num)
equal_count = 0
i = 0
while i < len(seq):
    j = i + 1
    while j < len(seq) and seq[j] == seq[i]:
        j += 1
    if j - i > 1:
        equal_count += (j - i)
    i = j
print(f"Количество чисел, идущих подряд и равных между собой: {equal_count}")
