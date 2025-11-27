num = int(input("7-значное число: "))
reversed_num = 0
for _ in range(7):
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print("Число наоборот:", reversed_num)
