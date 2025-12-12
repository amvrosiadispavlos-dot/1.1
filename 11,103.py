import random
arr = [random.randint(1, 100) for _ in range(20)]
print("Массив:", arr)
max_sum = 0
start_index = 0
for i in range(len(arr)-4):
    current_sum = sum(arr[i:i+5])
    if current_sum > max_sum:
        max_sum = current_sum
        start_index = i
print(f"Максимальная сумма 5 соседних элементов: {max_sum}")
print(f"Элементы: {arr[start_index:start_index+5]}")
