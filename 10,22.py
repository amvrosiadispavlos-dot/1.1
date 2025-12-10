import random

suits = ["пики", "трефы", "бубны", "червы"]
ranks = ["шестерка", "семерка", "восьмерка", "девятка", "десятка", "валет", "дама", "король", "туз"]

def generate_card():
    suit = random.choice(suits)
    rank = random.choice(ranks)
    return suit, rank

def compare_cards(card1, card2):
    suit1, rank1 = card1
    suit2, rank2 = card2
    
    if suits.index(suit1) > suits.index(suit2):
        return 1
    elif suits.index(suit1) < suits.index(suit2):
        return 2
    else:
        if ranks.index(rank1) > ranks.index(rank2):
            return 1
        elif ranks.index(rank1) < ranks.index(rank2):
            return 2
        else:
            return 0

n = int(input("Сколько раз играем? "))
player1_wins = 0
player2_wins = 0
draws = 0

for i in range(n):
    card1 = generate_card()
    card2 = generate_card()
    
    print(f"\nИгра {i+1}:")
    print(f"Игрок 1: {card1[1]} {card1[0]}")
    print(f"Игрок 2: {card2[1]} {card2[0]}")
    
    result = compare_cards(card1, card2)
    if result == 1:
        print("Победил игрок 1")
        player1_wins += 1
    elif result == 2:
        print("Победил игрок 2")
        player2_wins += 1
    else:
        print("Ничья")
        draws += 1

print(f"\nИтог: Игрок 1 - {player1_wins}, Игрок 2 - {player2_wins}, Ничьих - {draws}")
