import random
player1 = random.randint(1, 6)
player2 = random.randint(1, 6)
print(f"Игрок 1: {player1}")
print(f"Игрок 2: {player2}")
if player1 > player2:
    print("Победил игрок 1")
elif player2 > player1:
    print("Победил игрок 2")
else:
    print("Ничья")
