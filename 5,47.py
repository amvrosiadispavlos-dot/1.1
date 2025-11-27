n = int(input("n (≥4) = "))
v = [0, 0, 1.5] 
for i in range(4, n + 1):
    v_i = ((i - 1) / (i**2 + 1)) * v[i-2] - v[i-3] + v[i-4]
    v.append(v_i)
print(f"v{n} = {v[n-1]}")
