ages = list(map(int, input("Введите возраст людей через пробел: ").split()))
oldest = max(ages)
youngest = min(ages)
oldest_first_index = -1
youngest_first_index = -1
for i in range(len(ages)):
    if ages[i] == oldest and oldest_first_index == -1:
        oldest_first_index = i
    if ages[i] == youngest and youngest_first_index == -1:
        youngest_first_index = i
if oldest_first_index < youngest_first_index:
    print("Самый старший указан раньше самого молодого")
else:
    print("Самый молодой указан раньше самого старшего")
