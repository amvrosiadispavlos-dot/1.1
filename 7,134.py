print("Введите невозрастающую последовательность вещественных чисел, оканчивающуюся 0:")
seq = []
while True:
    num = float(input())
    if num == 0:
        break
    seq.append(num)
unique_count = 1 if seq else 0
for i in range(1, len(seq)):
    if seq[i] != seq[i-1]:
        unique_count += 1
print(f"Количество различных чисел: {unique_count}")
