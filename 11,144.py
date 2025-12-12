import random
residents = [random.randint(1, 10) for _ in range(15)]
sorted_floors = sorted(enumerate(residents), key=lambda x: x[1])
least_two = sorted_floors[:2]
print(f"Два этажа с наименьшим числом жителей:")
for floor, count in least_two:
    print(f"Этаж {floor+1}: {count} человек")
