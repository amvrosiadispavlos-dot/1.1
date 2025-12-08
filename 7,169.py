n = int(input("Введите количество этапов: "))
times = list(map(float, input("Введите результаты на каждом этапе (в минутах) через пробел: ").split()[:n]))
win_time = min(times)
lose_time = max(times)
win_index = -1
lose_index = -1
for i in range(n):
    if times[i] == win_time and win_index == -1:
        win_index = i
    if times[i] == lose_time and lose_index == -1:
        lose_index = i
if win_index < lose_index:
    print("Да, этап победы был раньше этапа последнего места")
else:
    print("Нет, этап победы был позже этапа последнего места")
