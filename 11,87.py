arr = [5, 12, 8, 20, 3, 15, 9, 25]
selected = [x for x in arr if x > 10]
avg = sum(selected) / len(selected) if selected else 0
print(f"Среднее элементов >10: {avg:.2f}")
