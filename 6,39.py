num = int(input("n = "))
digits = []
if num == 0:
    digits = [0]
else:
    temp = abs(num)
    while temp > 0:
        digits.append(temp % 10)
        temp //= 10
    digits.reverse()
for digit in digits:
    print(digit)
