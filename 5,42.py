distance = 0
sign = 1
for i in range(1, 101):
    distance += sign * (1 / i)
    sign = -sign  
print("Расстояние от дома после 100 этапа:", abs(distance), "км")
total_path = 0

for i in range(1, 101):
    total_path += 1 / i
print("Общий пройденный путь:", total_path, "км")
