print("Введите последовательность целых чисел, оканчивающуюся 9999:")
seq = []
while True:
    num = int(input())
    if num == 9999:
        break
    seq.append(num)
found = False
for i in range(len(seq) - 1):
    if seq[i] % 2 == 0 and seq[i+1] % 2 == 0:
        print(f"Найдена пара соседних чётных чисел на позициях {i+1} и {i+2}")
        found = True
        break
if not found:
    print("Нет пар соседних чётных чисел")
