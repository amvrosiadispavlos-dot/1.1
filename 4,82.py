n = int(input("n (1-99) = "))
if 11 <= n <= 19:
    ending = "лет"
else:
    last_digit = n % 10
    if last_digit == 1:
        ending = "год"
    elif 2 <= last_digit <= 4:
        ending = "года"
    else:
        ending = "лет"
print(f"мне {n} {ending}")
