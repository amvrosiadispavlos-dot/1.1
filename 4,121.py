x = float(input("x = "))
if x < 1:
    region = "I"
elif x <= 5:
    region = "II"
else:
    region = "III"
print("Точка попадает в область:", region)
