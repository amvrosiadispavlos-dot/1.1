n = int(input("Введите порядковый номер n (1..50): "))
cols = 5
row = (n - 1) // cols + 1
col = (n - 1) % cols + 1
print("Строка:", row)
print("Столбец:", col)
