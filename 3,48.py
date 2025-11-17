y = float(input("Угол поворота часовой стрелки (0 ≤ y ≤ 360): "))
hours = int(y // 30)
remainder_degrees = y % 30
minutes = int(remainder_degrees * 2)
print(f"Прошло: {hours} полных часов, {minutes} полных минут")
