grades = list(map(int, input("Введите 20 оценок через пробел (сначала все 5, потом остальные): ").split()[:20]))
count_5 = 0
for grade in grades:
    if grade == 5:
        count_5 += 1
    else:
        break  
print(f"Количество учеников с оценкой 5 (случай 1): {count_5}")
grades = list(map(int, input("Введите 20 оценок через пробел (сначала все 5, потом остальные): ").split()[:20]))
count_5 = 0
for grade in grades:
    if grade == 5:
        count_5 += 1
    else:
        break 
print(f"Количество учеников с оценкой 5 (случай 2): {count_5}")
