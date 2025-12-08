def bisection(f, a, b, eps=0.001):
    if f(a) * f(b) > 0:
        return None
    while b - a > eps:
        mid = (a + b) / 2
        if f(mid) == 0:
            return mid
        if f(a) * f(mid) < 0:
            b = mid
        else:
            a = mid
    return (a + b) / 2
f1 = lambda x: x**4 + 2*x**3 - x - 1
root1 = bisection(f1, 0, 1)
print(f"а) Корень на [0, 1]: {root1:.4f}")
f2 = lambda x: x**3 - 0.2*x**2 - 0.2**x - 1.2
root2 = bisection(f2, 1, 1.5)
print(f"б) Корень на [1, 1.5]: {root2:.4f}")
