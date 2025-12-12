arr = [2, 8, 5, 12, 7, 9]
avg = sum(arr) / len(arr)
closest = min(arr, key=lambda x: abs(x - avg))
print(f"Среднее: {avg:.2f}")
print(f"Ближайший элемент: {closest}")
