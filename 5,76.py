a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

for num in range(a, b + 1):
    if num % c == 0:
        print(num, end=" ")
print()
