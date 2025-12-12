arr = [3, -5, 10, -2, 0, 7, -8]
non_negative = [x for x in arr if x >= 0]
negative = [x for x in arr if x < 0]
print("Сначала неотрицательные:", non_negative)
print("Затем отрицательные:", negative)
