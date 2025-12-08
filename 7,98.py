numbers = list(map(int, input("Введите 20 натуральных чисел через пробел: ").split()[:20]))
found = False
for i in range(len(numbers) - 1):
    if numbers[i] % 2 == 1 and numbers[i+1] % 2 == 1:
        print(f"Найдена пара соседних нечётных чисел на позициях {i+1} и {i+2}")
        found = True
        break
if not found:
    print("Нет пар соседних нечётных чисел")
