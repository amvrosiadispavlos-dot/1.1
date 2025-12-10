limit = 30
solutions = set()
for x in range(1, limit+1):
    for y in range(x, limit+1):
        k2 = x**2 + y**2
        k = int(k2**0.5)
        if k <= limit and k**2 == k2:
            solutions.add((x, y, k))
for sol in sorted(solutions):
    print(f"{sol[0]}^2 + {sol[1]}^2 = {sol[2]}^2")
