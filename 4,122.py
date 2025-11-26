y = float(input("y = "))
if y > 5.0:
    region = "I"
elif y >= 2.5:
    region = "II"
else:
    region = "III"
print("Точка попадает в область:", region)
