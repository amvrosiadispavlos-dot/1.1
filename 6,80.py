n = input("Введите натуральное число: ")
increasing = True
for i in range(len(n)-1):
    if n[i] >= n[i+1]:
        increasing = False
        break
print(f"Цифры слева направо упорядочены по возрастанию: {increasing}")
