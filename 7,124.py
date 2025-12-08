points = list(map(int, input("Введите очки 20 команд по убыванию через пробел: ").split()[:20]))
N = int(input("Введите количество очков команды N: "))
place = 1
i = 0
while i < 20 and points[i] > N:
    place += 1
    i += 1
print(f"Команда с {N} очками заняла {place}-е место.")
