n = int(input("n = "))
first_odd = n * (n - 1) + 1  
cube = 0
for i in range(n):
    cube += first_odd + 2 * i
print(f"{n}³ = {cube}")
