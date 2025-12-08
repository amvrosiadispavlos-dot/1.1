n = input("Введите натуральное число с разными цифрами: ")
max1 = max2 = -1
max1_pos_start = max2_pos_start = -1
max1_pos_end = max2_pos_end = -1
min1 = 10
min2 = 10
min1_pos_start = min2_pos_start = -1
min1_pos_end = min2_pos_end = -1
for i, char in enumerate(n):
    d = int(char)
    pos_start = i + 1
    pos_end = len(n) - i
    if d > max1:
        max2 = max1
        max2_pos_start = max1_pos_start
        max2_pos_end = max1_pos_end
        max1 = d
        max1_pos_start = pos_start
        max1_pos_end = pos_end
    elif d > max2:
        max2 = d
        max2_pos_start = pos_start
        max2_pos_end = pos_end
    if d < min1:
        min2 = min1
        min2_pos_start = min1_pos_start
        min2_pos_end = min1_pos_end
        min1 = d
        min1_pos_start = pos_start
        min1_pos_end = pos_end
    elif d < min2:
        min2 = d
        min2_pos_start = pos_start
        min2_pos_end = pos_end
print("а) Порядковые номера двух максимальных цифр:")
print(f"   Максимальная {max1}: от начала - {max1_pos_start}, от конца - {max1_pos_end}")
print(f"   Вторая максимальная {max2}: от начала - {max2_pos_start}, от конца - {max2_pos_end}")
print("б) Порядковые номера двух минимальных цифр:")
print(f"   Минимальная {min1}: от начала - {min1_pos_start}, от конца - {min1_pos_end}")
print(f"   Вторая минимальная {min2}: от начала - {min2_pos_start}, от конца - {min2_pos_end}")
