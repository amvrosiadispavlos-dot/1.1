def is_geometric(m, first, ratio):
    if first == 0:
        return m == 0
    if ratio == 0:
        return m == first or m == 0
    if m == 0:
        return first == 0
    q = m / first
    return q > 0 and (q ** (1/ratio)).is_integer()
g = float(input("Первый член прогрессии: "))
z = float(input("Знаменатель прогрессии: "))
m = float(input("Проверяемое число: "))
if is_geometric(m, g, z):
    print(f"{m} может быть членом геометрической прогрессии")
else:
    print(f"{m} не является членом геометрической прогрессии")
