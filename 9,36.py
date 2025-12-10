s = int(input("Введите площадь s: "))
print("а) Разные решения (с перестановкой):")
for a in range(1, s+1):
    if s % a == 0:
        b = s // a
        print(f"  {a} x {b}")
print("б) Совпадающие решения (без перестановки):")
for a in range(1, int(s**0.5)+1):
    if s % a == 0:
        b = s // a
        print(f"  {a} x {b}")
