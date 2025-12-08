numbers = list(map(float, input("Введите 15 вещественных чисел через пробел: ").split()[:15]))
count_le = sum(1 for x in numbers if x <= 33.2)
print(f"Количество чисел ≤ 33.2 = {count_le}, кратно 4: {count_le % 4 == 0}")
