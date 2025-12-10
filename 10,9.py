import random

for trials in [100, 1000]:
    counts = {0: 0, 1: 0}
    for _ in range(trials):
        result = random.randint(0, 1)
        counts[result] += 1
    
    print(f"\nПри {trials} подбрасываниях:")
    print(f"0 (орёл): {counts[0]} раз, частота: {counts[0]/trials:.3f}")
    print(f"1 (решка): {counts[1]} раз, частота: {counts[1]/trials:.3f}")
