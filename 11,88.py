arr = [15, 25, 8, 30, 5, 20, 12]
m = 20
selected = [x for x in arr if x < m]
avg = sum(selected) / len(selected) if selected else 0
print(f"Среднее элементов <{m}: {avg:.2f}")
