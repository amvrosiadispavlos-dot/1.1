n = int(input("Введите количество троек n: "))
count_triangles = 0
for i in range(n):
    print(f"Тройка {i+1}:")
    a, b, c = map(int, input("  Введите a b c (через пробел): ").split())
    if a + b > c: 
        count_triangles += 1
print(f"Количество троек, из которых можно построить треугольник: {count_triangles}")
