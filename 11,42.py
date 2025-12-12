arr = [2, 4, 6, 8, 10, 12, 14, 16]
print("Массив:", arr)

# а)
total_sum = sum(arr)
print(f"а) Сумма всех элементов: {total_sum}")

# б)
product = 1
for x in arr:
    product *= x
print(f"б) Произведение всех элементов: {product}")

# в)
sum_of_squares = sum(x**2 for x in arr)
print(f"в) Сумма квадратов: {sum_of_squares}")

# г)
sum_first_six = sum(arr[:6])
print(f"г) Сумма первых шести элементов: {sum_first_six}")

# д)
k1 = int(input("Введите k1: "))
k2 = int(input("Введите k2 (k2 > k1): "))
if 0 <= k1 < len(arr) and 0 <= k2 < len(arr) and k2 > k1:
    sum_range = sum(arr[k1:k2+1])
    print(f"д) Сумма элементов с {k1} по {k2}: {sum_range}")

# е)
average = sum(arr) / len(arr)
print(f"е) Среднее арифметическое всех элементов: {average:.2f}")

# ж)
s1 = int(input("Введите s1: "))
s2 = int(input("Введите s2 (s2 > s1): "))
if 0 <= s1 < len(arr) and 0 <= s2 < len(arr) and s2 > s1:
    avg_range = sum(arr[s1:s2+1]) / (s2 - s1 + 1)
    print(f"ж) Среднее арифметическое элементов с {s1} по {s2}: {avg_range:.2f}")
