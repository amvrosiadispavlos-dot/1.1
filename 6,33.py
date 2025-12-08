yield_per_ha = 20
year = 1
while yield_per_ha <= 22:
    year += 1
    yield_per_ha *= 1.02
print(f"Урожайность >22 ц/га в {year} году")
area = 100
year = 1
while area <= 120:
    year += 1
    area *= 1.05
print(f"Площадь >120 га в {year} году")
area = 100
yield_per_ha = 20
total_harvest = area * yield_per_ha
year = 1
while total_harvest <= 800:
    year += 1
    area *= 1.05
    yield_per_ha *= 1.02
    total_harvest += area * yield_per_ha
print(f"Общий урожай >800 ц в {year} году")
