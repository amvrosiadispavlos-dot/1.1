arr = [3.5, -2.1, 7.8, 4.3, -1.2, 6.5, 8.9, 2.4, 9.1, 5.6]
positive_count = sum(1 for x in arr if x > 0)
le_50_55_count = sum(1 for x in arr if x <= 50.55)
print(f"а) Положительных ≤5: {positive_count <= 5}")
print(f"б) Количество ≤50.55 кратно 4: {le_50_55_count % 4 == 0}")
