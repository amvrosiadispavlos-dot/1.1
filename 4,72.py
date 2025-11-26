x1_1 = float(input("x1 левый нижний первого: "))
y1_1 = float(input("y1 левый нижний первого: "))
w1 = float(input("ширина первого: "))
h1 = float(input("высота первого: "))
x1_2 = float(input("x1 левый нижний второго: "))
y1_2 = float(input("y1 левый нижний второго: "))
w2 = float(input("ширина второго: "))
h2 = float(input("высота второго: "))
x2_1 = x1_1 + w1
y2_1 = y1_1 + h1
x2_2 = x1_2 + w2
y2_2 = y1_2 + h2
first_in_second = (x1_1 >= x1_2 and y1_1 >= y1_2 and 
                   x2_1 <= x2_2 and y2_1 <= y2_2)
print("а) Первый внутри второго:", first_in_second)
second_in_first = (x1_2 >= x1_1 and y1_2 >= y1_1 and 
                   x2_2 <= x2_1 and y2_2 <= y2_1)
one_inside_other = first_in_second or second_in_first
print("б) Один внутри другого:", one_inside_other)
intersect = not (x2_1 < x1_2 or x2_2 < x1_1 or 
                 y2_1 < y1_2 or y2_2 < y1_1)
print("в) Прямоугольники пересекаются:", intersect)
