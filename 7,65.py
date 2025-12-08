n = int(input("Введите количество команд: "))
count_better = 0
for i in range(n):
    wins = int(input(f"Введите количество выигрышей команды {i+1}: "))
    losses = int(input(f"Введите количество проигрышей команды {i+1}: "))
    if wins > losses:
        count_better += 1
print(f"Команд с выигрышей больше, чем проигрышей: {count_better}")
