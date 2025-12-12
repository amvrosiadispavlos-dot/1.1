heights = [185, 182, 180, 178, 175, 173, 170, 168, 165, 163]
new1, i1 = 176, 4
new2, i2 = 142, 8
heights.insert(i1, new1)
if i2 >= i1:
    i2 += 1
heights.insert(i2, new2)
result = sorted(heights, reverse=True)
print(f"Исходный: [185, 182, 180, 178, 175, 173, 170, 168, 165, 163]")
print(f"Результат: {result}")

heights = [185, 182, 180, 178, 175, 173, 170, 168, 165, 163]
new1, new2 = 176, 142
heights.append(new1)
heights.append(new2)
result = sorted(heights, reverse=True)
print(f"Исходный: [185, 182, 180, 178, 175, 173, 170, 168, 165, 163]")
print(f"Результат: {result}")
