import random
ages = [random.randint(20, 80) for _ in range(30)]
oldest = min(ages) 
youngest = max(ages)
oldest_index = ages.index(oldest)
youngest_index = ages.index(youngest)
if oldest_index < youngest_index:
    print("Самый старый указан раньше")
elif youngest_index < oldest_index:
    print("Самый молодой указан раньше")
else:
    print("Самый старый и самый молодой — один человек")
