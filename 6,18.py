import math
a = int(input("a (большее) = "))
b = int(input("b (меньшее) = "))
x = a
while x >= b:
    print(math.sqrt(x))
    x -= 1
import math
a = int(input("a (большее) = "))
b = int(input("b (меньшее) = "))
x = a
while True:
    print(math.sqrt(x))
    x -= 1
    if x < b:
        break
