print("Фунты | Кг")
print("-" * 12)
for pounds in range(1, 11):
    kg = pounds * 0.453 
    print(f"{pounds:2d}    | {kg:.3f}")
