m = int(input("m = "))
n = int(input("n = "))
limit = m * n
num = m
while num <= limit:
    print(num, end=" ")
    num += m
print()
num = n
while num <= limit:
    print(num, end=" ")
    num += n
