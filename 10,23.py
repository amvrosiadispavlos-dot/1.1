import random

suits = ["пики", "трефы", "бубны", "червы"]
ranks = ["шестерка", "семерка", "восьмерка", "девятка", "десятка", "валет", "дама", "король", "туз"]

trump_suit = random.choice(suits)
print(f"Козырная масть: {trump_suit}")

def generate_card():
    suit = random.choice(suits)
    rank = random.choice(ranks)
    return suit, rank

def compare_cards(card1, card2):
    suit1, rank1 = card1
    suit2, rank2 = card2
    
    # Проверка козырей
    trump1 = suit1 == trump_suit
    trump2 = suit2 == trump_suit
    
    if trump1 and not trump2:
        return 1
    elif not trump1 and trump2:
        return 2
    elif trump1 and trump2:
        # Оба козыри - сравниваем достоинства
        if ranks.index(rank1) > ranks.index(rank2):
            return 1
        elif ranks.index(rank1) < ranks.index(rank2):
            return 2
        else:
            return 0
    else:
        # Ни один не козырь - обычное сравнение
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

card1 = generate_card()
card2 = generate_card()

print(f"\nИгрок 1: {card1[1]} {card1[0]}")
print(f"Игрок 2: {card2[1]} {card2[0]}")

result = compare_cards(card1, card2)
if result == 1:
    print("Победил игрок 1")
elif result == 2:
    print("Победил игрок 2")
else:
    print("Карты равны по старшинству")
