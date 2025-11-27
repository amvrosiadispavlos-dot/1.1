n = int(input("n = "))
a = [0] * (n + 1)
a[0] = 1
print("a₀ =", a[0])
for k in range(1, n + 1):
    a[k] = k * a[k - 1] + 1 / k
    print(f"a{k} = {a[k]}")
