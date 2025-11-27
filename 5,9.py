print("Дюймы | Сантиметры")
print("-" * 18)
for inches in range(10, 23):
    cm = inches * 2.54  
    print(f"{inches:2d}    | {cm:6.2f}")
