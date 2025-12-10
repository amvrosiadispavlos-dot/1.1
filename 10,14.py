import random

K = int(input("Сколько кубиков бросает каждый игрок? "))
players = 3
scores = []

for player in range(players):
    total = sum(random.randint(1, 6) for _ in range(K))
    scores.append(total)
    print(f"Игрок {player+1}: {total} очков")

max_score = max(scores)
winners = [i+1 for i, score in enumerate(scores) if score == max_score]

if len(winners) == 1:
    print(f"Победил игрок {winners[0]}")
else:
    print(f"Ничья между игроками: {', '.join(map(str, winners))}")
