v = int(input("Введите объём v: "))
print("а) Разные решения (с перестановкой):")
for a in range(1, v+1):
    for b in range(1, v+1):
        if v % (a*b) == 0:
            c = v // (a*b)
            if c >= 1 and a*b*c == v:
                print(f"  {a} x {b} x {c}")
print("б) Совпадающие решения (без перестановки):")
found = set()
for a in range(1, int(v**(1/3))+1):
    if v % a == 0:
        for b in range(a, int((v//a)**0.5)+1):
            if (v//a) % b == 0:
                c = (v//a)//b
                if c >= b:
                    triple = tuple(sorted([a, b, c]))
                    if triple not in found:
                        found.add(triple)
                        print(f"  {a} x {b} x {c}")
