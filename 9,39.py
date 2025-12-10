m = int(input("Введите m: "))
n = int(input("Введите n: "))
total = sum(i**n for i in range(1, m+1))
print(total)
