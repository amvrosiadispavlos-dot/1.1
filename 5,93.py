n = int(input("n = "))
divisor_sum = 0
for i in range(1, n):
    if n % i == 0:
        divisor_sum += i
print("Число совершенное:", divisor_sum == n)
