print("Вводите удаления: номер команды (1 или 2) и длительность (2, 5, 10). Для окончания введите 0 0")
removals_team1 = 0
time_team1 = 0
removals_team2 = 0
time_team2 = 0
while True:
    try:
        team, minutes = map(int, input().split())
        if team == 0 and minutes == 0:
            break
        if team == 1:
            removals_team1 += 1
            time_team1 += minutes
        elif team == 2:
            removals_team2 += 1
            time_team2 += minutes
    except:
        break
print(f"Команда 1: удалений {removals_team1}, штрафное время {time_team1} мин")
print(f"Команда 2: удалений {removals_team2}, штрафное время {time_team2} мин")
