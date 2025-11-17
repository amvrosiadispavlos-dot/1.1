num = int(input("Введите трехзначное число с разными цифрами: "))
h = num // 100
t = (num // 10) % 10
u = num % 10
print("Все перестановки:")
print(h, t, u, "->", h*100 + t*10 + u)
print(h, u, t, "->", h*100 + u*10 + t)
print(t, h, u, "->", t*100 + h*10 + u)
print(t, u, h, "->", t*100 + u*10 + h)
print(u, h, t, "->", u*100 + h*10 + t)
print(u, t, h, "->", u*100 + t*10 + h)
