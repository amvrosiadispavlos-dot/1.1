a = int(input("a (час прибытия): "))
b = int(input("b (минута прибытия): "))
c = int(input("c (час отправления): "))
d = int(input("d (минута отправления): "))
n = int(input("n (час пассажира): "))
m = int(input("m (минута пассажира): "))
arrival = a * 60 + b
departure = c * 60 + d
passenger = n * 60 + m
train_on_platform = arrival <= passenger < departure
print(f"Поезд будет стоять на платформе: {train_on_platform}")
