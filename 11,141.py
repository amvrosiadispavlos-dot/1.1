import random
birth_years = [random.randint(1950, 2010) for _ in range(30)]
sorted_years = sorted(birth_years)  
oldest_two = sorted_years[:2]
print(f"Годы рождения двух самых старших: {oldest_two}")
