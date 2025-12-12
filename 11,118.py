import random
birth_years = [random.randint(1970, 2005) for _ in range(30)]
oldest = min(birth_years)
youngest = max(birth_years)
current_year = 2025
age_difference = (current_year - oldest) - (current_year - youngest)
print(f"Год рождения самого старого: {oldest}")
print(f"Год рождения самого молодого: {youngest}")
print(f"Разница в возрасте: {age_difference} лет")
