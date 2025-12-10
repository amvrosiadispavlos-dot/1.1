def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
nums = list(map(int, input("Введите натуральные числа через пробел: ").split()))
current_gcd = nums[0]
for num in nums[1:]:
    current_gcd = gcd(current_gcd, num)
print(f"НОД всех чисел: {current_gcd}")
