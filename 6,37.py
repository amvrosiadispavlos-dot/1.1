num = int(input("n = "))
temp = abs(num)
position = 0
found_position = 0
while temp > 0:
    position += 1
    if temp % 10 == 8:
        found_position = position
    temp //= 10
print("Номер цифры 8 от конца:", found_position)
