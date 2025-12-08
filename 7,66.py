print("Введите последовательность вещественных чисел, начинающуюся с отрицательного:")
seq = list(map(float, input().split()))
count_neg_start = 0
for num in seq:
    if num < 0:
        count_neg_start += 1
    else:
        break 
print(f"Количество отрицательных чисел в начале: {count_neg_start}")
