print("Введите последовательность целых чисел, оканчивающуюся -1:")
seq = []
while True:
    num = int(input())
    if num == -1:
        break
    seq.append(num)
found = False
for i in range(len(seq) - 1):
    if seq[i] == seq[i+1]:
        print(f"Найдена пара одинаковых соседних чисел на позициях {i+1} и {i+2}")
        found = True
        break
if not found:
    print("Нет пар одинаковых соседних чисел")
