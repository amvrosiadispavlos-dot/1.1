num = int(input("n = "))
temp = abs(num)
position = 0
found_position = 0
while temp > 0:
    position += 1
    if temp % 10 == 3:
        found_position = position
        break
print("Номер цифры 3 от конца:", found_position)
