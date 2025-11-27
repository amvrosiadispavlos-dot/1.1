import math
thickness = 0.5 
inner_diameter = 10 
total_volume = 0
for i in range(12):
    diameter = inner_diameter + 2 * i * thickness
    volume = (4/3) * math.pi * (diameter/2)**3
    total_volume += volume
total_liters = total_volume / 1000
print(f"Суммарный объем: {total_liters:.2f} л")
