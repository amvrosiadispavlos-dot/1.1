n = input("Введите натуральное число: ")
non_decreasing = True
for i in range(len(n)-1):
    if n[i] < n[i+1]:
        non_decreasing = False
        break
print(f"Цифры справа налево упорядочены по неубыванию: {non_decreasing}")
