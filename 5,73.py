import math
length = 4.5
initial_distance = 3
print("Расстояние | Угол (градусы)")
print("-" * 25)
distance = initial_distance
while distance > 0:
    angle = math.degrees(math.acos(distance / length))
    print(f"{distance:6.1f}    | {angle:6.1f}")
    distance -= 0.2
    if distance < 0:
        distance = 0
        angle = math.degrees(math.acos(distance / length))
        print(f"{distance:6.1f}    | {angle:6.1f}")
