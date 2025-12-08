n = int(input("Введите количество учеников в классе: "))
grades = list(map(int, input("Введите оценки по алгебре через пробел: ").split()[:n]))
average = sum(grades) / n
print("Средняя оценка по алгебре:", average)
