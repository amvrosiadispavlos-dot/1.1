n = input("Введите натуральное число: ")
ordered = True
for i in range(len(n)-1):
    if n[i] <= n[i+1]: 
        ordered = False
        break
print(f"Цифры справа налево упорядочены по возрастанию: {ordered}")
