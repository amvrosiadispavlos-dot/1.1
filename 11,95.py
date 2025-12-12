arr = [5, 12, 3, 8, 20, 6]
total = sum(arr)
indices = [i for i, x in enumerate(arr) if x > total]
print(f"Сумма всех элементов: {total}")
print(f"Количество элементов > суммы: {len(indices)}")
print(f"Их индексы: {indices}")
