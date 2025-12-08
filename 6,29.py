count = 0
num = 100
while count < 10:
    if num % 9 == 0 and num % 10 == 7:
        print(num, end=" ")
        count += 1
    num += 1
print()
