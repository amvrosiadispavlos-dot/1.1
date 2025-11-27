price_per_kg = float(input("Стоимость 1 кг конфет (руб): "))
print("Вес (г) | Стоимость (руб)")
print("-" * 23)
for weight in range(100, 2001, 100):
    cost = (weight / 1000) * price_per_kg
    print(f"{weight:4d}    | {cost:6.2f}")
