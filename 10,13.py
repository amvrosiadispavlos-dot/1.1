import random

player1_roll1 = random.randint(1, 6)
player1_roll2 = random.randint(1, 6)
player2_roll1 = random.randint(1, 6)
player2_roll2 = random.randint(1, 6)

player1_total = player1_roll1 + player1_roll2
player2_total = player2_roll1 + player2_roll2

print(f"Игрок 1: {player1_roll1} + {player1_roll2} = {player1_total}")
print(f"Игрок 2: {player2_roll1} + {player2_roll2} = {player2_total}")

if player1_total > player2_total:
    print("Победил игрок 1")
elif player2_total > player1_total:
    print("Победил игрок 2")
else:
    print("Ничья")

import random

n = int(input("Сколько раз бросать кубики? "))
player1_wins = 0
player2_wins = 0
draws = 0

for i in range(n):
    player1_roll1 = random.randint(1, 6)
    player1_roll2 = random.randint(1, 6)
    player2_roll1 = random.randint(1, 6)
    player2_roll2 = random.randint(1, 6)
    
    player1_total = player1_roll1 + player1_roll2
    player2_total = player2_roll1 + player2_roll2
    
    if player1_total > player2_total:
        player1_wins += 1
    elif player2_total > player1_total:
        player2_wins += 1
    else:
        draws += 1

print(f"\nРезультаты после {n} игр:")
print(f"Игрок 1 выиграл: {player1_wins} раз")
print(f"Игрок 2 выиграл: {player2_wins} раз")
print(f"Ничья: {draws} раз")
