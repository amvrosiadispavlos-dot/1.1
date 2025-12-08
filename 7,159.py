n = int(input("Введите количество квартир: "))
residents = list(map(int, input("Введите количество жильцов в каждой квартире через пробел: ").split()[:n]))
max_residents = max(residents)
last_apartment = -1
for i in range(n):
    if residents[i] == max_residents:
        last_apartment = i + 1
print(f"Квартира с максимальным числом жильцов (последняя): №{last_apartment}")
