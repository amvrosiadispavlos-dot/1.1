n = int(input("n (1-32) = "))
seq = ""
for num in range(0, 21):  
    seq += str(num)
digit = seq[n - 1]
print(f"{n}-я цифра: {digit}")
