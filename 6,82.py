n = input("Введите натуральное число: ")
non_decreasing_left = True
for i in range(len(n)-1):
    if n[i] > n[i+1]:
        non_decreasing_left = False
        break
print(f"Цифры слева направо упорядочены по неубыванию: {non_decreasing_left}")
