yield_per_ha = 20  # ц/га
print("Год | Урожайность (ц/га)")
print("-" * 22)
for year in range(1, 9):
    if year > 1:
        yield_per_ha *= 1.02 
    print(f"{year}   | {yield_per_ha:6.2f}")
area = 100  
print("Год | Площадь (га)")
print("-" * 15)
for year in range(1, 8):
    if year > 1:
        area *= 1.05  
    if year >= 4:
        print(f"{year}   | {area:6.2f}")
area = 100
yield_per_ha = 20
total_harvest = 0
for year in range(1, 7):
    harvest = area * yield_per_ha
    total_harvest += harvest
    area *= 1.05
    yield_per_ha *= 1.02
print(f"Урожай за 6 лет: {total_harvest:.2f} ц")
