x = float(input("x = "))
y = float(input("y = "))
R2 = 16 
in_circle = (x**2 + y**2 < R2)
in_I = (x > 0 and y > 0)
in_III = (x < 0 and y < 0)
if in_circle and (in_I or in_III):
    print("Точка попадает в область I или III")
else:
    print("Точка не попадает в область I или III")
