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
    
    # Сравниваем масти
    if suits.index(suit1) > suits.index(suit2):
        return 1
    elif suits.index(suit1) < suits.index(suit2):
        return 2
    else:
        # Масти равны, сравниваем достоинства
        if ranks.index(rank1) > ranks.index(rank2):
            return 1
        elif ranks.index(rank1) < ranks.index(rank2):
            return 2
        else:
            return 0

card1 = generate_card()
card2 = generate_card()

print(f"Игрок 1: {card1[1]} {card1[0]}")
print(f"Игрок 2: {card2[1]} {card2[0]}")

result = compare_cards(card1, card2)
if result == 1:
    print("Победил игрок 1")
elif result == 2:
    print("Победил игрок 2")
else:
    print("Карты равны по старшинству")
