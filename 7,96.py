numbers = list(map(int, input("Введите 15 натуральных чисел через пробел: ").split()[:15]))
found = False
for i in range(len(numbers) - 1):
    if numbers[i] == numbers[i+1]:
        print(f"Найдена пара одинаковых соседних чисел на позициях {i+1} и {i+2}")
        found = True
        break
if not found:
    print("Нет пар одинаковых соседних чисел")
