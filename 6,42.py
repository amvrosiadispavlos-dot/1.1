def max_min_digits(n):
    num = n
    max_d = min_d = num % 10
    while num > 0:
        d = num % 10
        if d > max_d: max_d = d
        if d < min_d: min_d = d
        num //= 10
    return max_d, min_d, max_d - min_d, max_d + min_d
