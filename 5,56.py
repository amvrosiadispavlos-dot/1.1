import math
n = 1000  
width = math.pi / n
area = 0
for i in range(n):
    x = i * width
    height = math.sin(x)
    area += height * width
print(f"Площадь арки синусоиды: {area:.4f}")
