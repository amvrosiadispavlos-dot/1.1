k = int(input("k (1-180) = "))
seq = ""
for num in range(10, 100):
    seq += str(num)
digit = seq[k - 1]
print(f"{k}-я цифра: {digit}")
