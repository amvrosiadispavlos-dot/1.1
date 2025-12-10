import random
suits = ["пик", "треф", "бубен", "червей"]
ranks = ["6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]

suit = random.choice(suits)
rank = random.choice(ranks)

print(f"Выбрана {rank} {suit}")
