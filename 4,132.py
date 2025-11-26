x = float(input("x = "))
y = float(input("y = "))
if x > 0 and y > 0:
    quarter = 1
elif x < 0 and y > 0:
    quarter = 2
elif x < 0 and y < 0:
    quarter = 3
else:  
    quarter = 4
print("Точка находится в", quarter, "четверти")
