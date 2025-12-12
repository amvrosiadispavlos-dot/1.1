import random
birth_years = [random.randint(1950, 2010) for _ in range(30)]
oldest_year = min(birth_years) 
# a)
first_index = birth_years.index(oldest_year)
# б)
last_index = len(birth_years) - 1 - birth_years[::-1].index(oldest_year)
print(f"Год рождения самого старшего: {oldest_year}")
print(f"a) Первый самый старший: {first_index+1}")
print(f"б) Последний самый старший: {last_index+1}")
