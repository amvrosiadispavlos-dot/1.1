print("Введите последовательность вещественных чисел (ввод прекратится после первого 0):")
count = 0
while True:
    num = float(input())
    if num == 0:
        break
    count += 1
print(f"Количество чисел перед первым нулём: {count}")
