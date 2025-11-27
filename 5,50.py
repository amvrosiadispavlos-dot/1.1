distance = 10  
print("День | Пробег (км)")
print("-" * 15)
for day in range(1, 11):
    if day > 1:
        distance *= 1.1 
    print(f"{day:2d}   | {distance:6.2f}")
distance = 10
total = 10  
for day in range(2, 8):
    distance *= 1.1
    total += distance
print(f"Суммарный путь за 7 дней: {total:.2f} км")
