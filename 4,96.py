k = int(input("k (1-252) = "))
seq = ""
for num in range(50, 251):
    seq += str(num)
digit = seq[k - 1]
print(f"{k}-я цифра: {digit}")
