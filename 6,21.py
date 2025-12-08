n = int(input("n (>9) = "))
while n >= 100:
    n //= 10
second_digit = n % 10
print("Вторая цифра:", second_digit)
