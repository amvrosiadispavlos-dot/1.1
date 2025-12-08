n = int(input("Введите количество чисел: "))
seq = []
for i in range(n):
    seq.append(int(input(f"Число {i+1}: ")))
max_len = 1
current_len = 1
direction = 0 
for i in range(1, n):
    if seq[i] > seq[i-1]:
        if direction == 1:
            current_len += 1
        else:
            direction = 1
            current_len = 2
    elif seq[i] < seq[i-1]:
        if direction == -1:
            current_len += 1
        else:
            direction = -1
            current_len = 2
    else:
        current_len = 1
        direction = 0
    
    if current_len > max_len:
        max_len = current_len
print(f"Наибольшая длина монотонного фрагмента: {max_len}")
seq = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
max_len = 1
current_len = 1
direction = 0
for i in range(1, len(seq)):
    if seq[i] > seq[i-1]:
        if direction == 1:
            current_len += 1
        else:
            direction = 1
            current_len = 2
    elif seq[i] < seq[i-1]:
        if direction == -1:
            current_len += 1
        else:
            direction = -1
            current_len = 2
    else:
        current_len = 1
        direction = 0
    if current_len > max_len:
        max_len = current_len
print(f"Наибольшая длина монотонного фрагмента: {max_len}")
