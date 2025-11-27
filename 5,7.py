price = 20.4
print("Количество | Стоимость")
print("-" * 20)
for quantity in range(2, 21):
    cost = price * quantity
    print(f"{quantity:2d}        | {cost:6.1f} руб.")
