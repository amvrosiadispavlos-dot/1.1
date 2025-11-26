x = float(input("x = "))
y = float(input("y = "))
abs_x = x if x >= 0 else -x
abs_y = y if y >= 0 else -y
half_sum = (abs_x + abs_y) / 2
print("а) Полусумма абсолютных величин:", half_sum)
from math import sqrt
root_product = sqrt(abs_x * abs_y)
print("б) Корень из произведения абсолютных величин:", root_product)
