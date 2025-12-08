count = 0
num = 500
while count < 20:
    if num % 13 == 0 or num % 17 == 0:
        print(num, end=" ")
        count += 1
    num += 1
print()
