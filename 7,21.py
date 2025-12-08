print("Введите результаты первого спортсмена (10 видов через пробел):")
scores1 = list(map(int, input().split()[:10]))
print("Введите результаты второго спортсмена (10 видов через пробел):")
scores2 = list(map(int, input().split()[:10]))
sum1 = sum(scores1)
sum2 = sum(scores2)
if sum1 > sum2:
    print(f"Первый спортсмен лучше: {sum1} > {sum2}")
elif sum2 > sum1:
    print(f"Второй спортсмен лучше: {sum2} > {sum1}")
else:
    print(f"Результаты равны: {sum1} = {sum2}")
