m = int(input("Введите длину последовательности m: "))
seq = list(map(int, input("Введите последовательность из 0 и 1 через пробел: ").split()[:m]))
min_len = float('inf')
current_len = 0
in_zero_segment = False
for bit in seq:
    if bit == 0:
        current_len += 1
        in_zero_segment = True
    else:
        if in_zero_segment:
            if current_len < min_len:
                min_len = current_len
            current_len = 0
            in_zero_segment = False
if in_zero_segment and current_len < min_len:
    min_len = current_len
if min_len == float('inf'):
    print("Нет отрезков из нулей")
else:
    print(f"Наименьшая длина отрезка из нулей: {min_len}")
