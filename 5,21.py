price_per_kg = float(input("Стоимость 1 кг сыра (руб): "))
print("Вес (г) | Стоимость (руб)")
print("-" * 23)
for weight in range(50, 1001, 50):
    cost = (weight / 1000) * price_per_kg
    print(f"{weight:4d}    | {cost:6.2f}")
