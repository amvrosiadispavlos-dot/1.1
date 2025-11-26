import math
g = 9.8
alpha = float(input("α (в градусах) = "))
v0 = float(input("v0 (м/с) = "))
R = float(input("R (м) = "))
H = float(input("H (м) = "))
P = float(input("P (м, высота цели) = "))
alpha_rad = math.radians(alpha)
t = R / (v0 * math.cos(alpha_rad))
y = v0 * t * math.sin(alpha_rad) - g * t**2 / 2
if H <= y <= H + P:
    print("Снаряд поразит цель")
else:
    print("Снаряд не поразит цель")
