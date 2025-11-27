n = int(input("n = "))
square = 0
odd = 1
for _ in range(n):
    square += odd
    odd += 2
print(f"{n}² = {square}")
