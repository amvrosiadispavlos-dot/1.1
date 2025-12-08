print("Вводите данные об удалениях: номер команды (1 или 2) и продолжительность в минутах.")
print("Для завершения введите 0 0")
total_time_team1 = 0
total_time_team2 = 0
total_removals = 0
while total_removals < 24:
    team, time = map(int, input(f"Удаление {total_removals + 1}: ").split())
    if team == 0 and time == 0:
        break
    if team == 1:
        total_time_team1 += time
    elif team == 2:
        total_time_team2 += time
    total_removals += 1
print(f"Общее время удалений команды 1: {total_time_team1} мин")
print(f"Общее время удалений команды 2: {total_time_team2} мин")
