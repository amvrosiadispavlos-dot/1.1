seq = list(map(int, input("Введите последовательность чисел без соседних одинаковых: ").split()))
max_len = 1
current_len = 1
for i in range(1, len(seq)):
    if seq[i] > seq[i-1]:
        current_len += 1
        if current_len > max_len:
            max_len = current_len
    else:
        current_len = 1
print(f"Наибольшая длина монотонно возрастающего фрагмента: {max_len}")
