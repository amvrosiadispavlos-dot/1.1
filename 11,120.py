import random
speeds = [random.randint(150, 300) for _ in range(40)]
max_speed = max(speeds)
# a)
first_index = speeds.index(max_speed)
# б)
last_index = len(speeds) - 1 - speeds[::-1].index(max_speed)
print(f"Самый быстрый автомобиль имеет скорость: {max_speed}")
print(f"a) Первый с такой скоростью имеет номер: {first_index+1}")
print(f"б) Последний с такой скоростью имеет номер: {last_index+1}")
