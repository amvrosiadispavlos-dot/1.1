print("Введите 20 чисел (например, 32 значит 3:2, 0 значит 0:0):")
wins = draws = losses = 0
points = 0
for i in range(20):
    num = int(input())
    scored = num // 10
    conceded = num % 10
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
    print(f"Игра {i+1}: {scored}:{conceded} – {result}")
print(f"\nВыигрышей: {wins}")
print(f"Ничьих: {draws}")
print(f"Проигрышей: {losses}")
print(f"Всего очков: {points}")
