a = float(input("Ребро кирпича a = "))
b = float(input("Ребро кирпича b = "))
c = float(input("Ребро кирпича c = "))
x = float(input("Сторона отверстия x = "))
y = float(input("Сторона отверстия y = "))
fit = (a <= x and b <= y) or (a <= y and b <= x) or \
      (a <= x and c <= y) or (a <= y and c <= x) or \
      (b <= x and c <= y) or (b <= y and c <= x)
print("Кирпич пройдет:", fit)
