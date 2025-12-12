import random
wins = [random.randint(0, 10) for _ in range(20)]
teams_with_few_wins = [i+1 for i, w in enumerate(wins) if w < 3]
print("Количество побед каждой команды:", wins)
print("Номера команд с <3 побед:", teams_with_few_wins)
