n = int(input("Введите количество учеников: "))
grades = list(map(int, input("Введите оценки через пробел: ").split()[:n]))
count_5 = grades.count(5)
print(f"Количество пятёрок: {count_5}")
