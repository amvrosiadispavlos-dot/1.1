print("Введите 20 пар чисел (забитые пропущенные) через пробел построчно или в одну строку:")
wins = draws = losses = 0
points = 0
for i in range(20):
    scored, conceded = map(int, input().split())
    if scored > conceded:
        result = "выигрыш"
        wins += 1
        points += 3
    elif scored == conceded:
        result = "ничья"
        draws += 1
        points += 1
    else:
        result = "проигрыш"
        losses += 1
    print(f"Игра {i+1}: {result}")
print("\nИтог:")
print(f"Выигрышей: {wins}")
print(f"Ничьих: {draws}")
print(f"Проигрышей: {losses}")
print(f"Всего очков: {points}")
