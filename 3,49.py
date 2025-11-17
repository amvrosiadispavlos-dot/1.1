import math
y = float(input("Угол часовой стрелки в радианах (0 < y ≤ 2π): "))
time_hours = y / (2 * math.pi) * 12
hours = int(time_hours)
fraction_hour = time_hours - hours
minutes = fraction_hour * 60
full_minutes = int(minutes)
minute_angle = (minutes / 60) * 2 * math.pi
print(f"Угол минутной стрелки: {minute_angle:.4f} рад")
print(f"Время: {hours} полных часов, {full_minutes} полных минут")
