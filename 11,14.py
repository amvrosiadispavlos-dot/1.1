n = int(input("Введите n (≤ 99999): "))
digits = [0] * 5 
temp = n
index = 0
while temp > 0:
    digits[index] = temp % 10
    temp //= 10
    index += 1
print("Цифры в обратном порядке:", digits[:index])
