k = int(input("k (1-222) = "))
seq = ""
for num in range(1, 111):  # от 1 до 110
    seq += str(num)
digit = seq[k - 1]
print(f"{k}-я цифра: {digit}")
