points = list(map(int, input("Введите очки команд через пробел: ").split()))
for i in range(len(points) - 1):
    if points[i] < points[i+1]:
        ordered = False
        print(f"Нарушение на позициях {i+1} и {i+2}")
        break
if ordered:
    print("Команды перечислены в соответствии с занятыми местами.")
else:
    print("Команды перечислены не в соответствии с местами.")
