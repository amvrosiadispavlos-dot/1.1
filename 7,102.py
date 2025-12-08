n = int(input("Введите количество учеников: "))
heights = list(map(float, input("Введите рост каждого ученика через пробел: ").split()[:n]))
for i in range(len(heights) - 1):
    if heights[i] < heights[i+1]:
        print(f"Ученики не перечислены в порядке убывания роста.")
        print(f"Нарушение на позициях {i+1} и {i+2}")
        break
else:
    print("Ученики перечислены в порядке убывания роста.")
