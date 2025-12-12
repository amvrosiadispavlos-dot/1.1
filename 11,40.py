import math
arr = [4, 9, 16, 25, 36]

# а)
index = 2
if 0 <= index < len(arr):
    print(f"а) Корень из элемента {index} ({arr[index]}): {math.sqrt(arr[index])}")

# б)
i1, i2 = 1, 3
if 0 <= i1 < len(arr) and 0 <= i2 < len(arr):
    avg = (arr[i1] + arr[i2]) / 2
    print(f"б) Среднее арифметическое элементов {i1} и {i2}: {avg}")
