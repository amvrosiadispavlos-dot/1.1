print("Введите последовательность целых чисел, оканчивающуюся отрицательным числом:")
seq = []
while True:
    num = int(input())
    if num < 0:
        break
    seq.append(num)
if seq:
    all_equal = all(x == seq[0] for x in seq)
    print(f"Все элементы последовательности равны: {all_equal}")
else:
    print("Последовательность пуста.")
