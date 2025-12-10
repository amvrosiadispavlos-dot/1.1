import random

for trials in [100, 1000]:
    counts = {i: 0 for i in range(1, 7)}
    for _ in range(trials):
        dice = random.randint(1, 6)
        counts[dice] += 1
    
    print(f"\nПри {trials} бросаниях:")
    for num in range(1, 7):
        freq = counts[num] / trials
        print(f"Число {num}: {counts[num]} раз, частота: {freq:.3f}")
