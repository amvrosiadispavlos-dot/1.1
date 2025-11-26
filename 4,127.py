a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if a > b and a > c:
    print("Самое большое: первое число")
elif b > a and b > c:
    print("Самое большое: второе число")
else:
    print("Самое большое: третье число")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if a < b and a < c:
    print("Самое малое: первое число")
elif b < a and b < c:
    print("Самое малое: второе число")
else:
    print("Самое малое: третье число")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if (b < a < c) or (c < a < b):
    print("Среднее: первое число")
elif (a < b < c) or (c < b < a):
    print("Среднее: второе число")
else:
    print("Среднее: третье число")
