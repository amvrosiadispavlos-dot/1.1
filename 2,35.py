v1 = float(input("Скорость первого автомобиля (км/ч): "))
v2 = float(input("Скорость второго автомобиля (км/ч): "))
s = float(input("Начальное расстояние между автомобилями (км): "))
if v1 <= v2:
    print("Ошибка: V1 должно быть больше V2")
else:
    time = 0.5
    distance1 = v1 * time
    distance2 = v2 * time
    new_distance = s + (distance1 - distance2)  
    print(f"Расстояние между автомобилями через 30 минут: {new_distance:.2f} км")
