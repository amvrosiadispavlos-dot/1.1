count = 0
while count < 10:
    num = int(input("Введите число: "))
    if num == 0:
        print("Ввод прекращён.")
        break
    count += 1
print(f"Введено чисел: {count}")
