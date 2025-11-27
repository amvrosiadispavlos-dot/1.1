a = float(input("a = "))
n = int(input("n = "))
result = 1
for i in range(1, n + 1):
    result *= a
    print(f"a^{i} = {result}")
