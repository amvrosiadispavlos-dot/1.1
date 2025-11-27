k = int(input("k = "))
num1, num2 = 1, 2  
den1, den2 = 1, 1  
if k == 1:
    print(f"{num1}/{den1}")
elif k == 2:
    print(f"{num2}/{den2}")
else:
    for _ in range(3, k + 1):
        num1, num2 = num2, num1 + num2
        den1, den2 = den2, den1 + den2
    print(f"{k}-й член: {num2}/{den2}")
n = int(input("n = "))
nums = [1, 2] 
dens = [1, 1]  
for i in range(2, n):
    nums.append(nums[i-1] + nums[i-2])
    dens.append(dens[i-1] + dens[i-2])
print("Первые", n, "членов:")
for i in range(n):
    print(f"{nums[i]}/{dens[i]}")
