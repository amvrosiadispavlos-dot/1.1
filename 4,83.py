k = int(input("k = "))
if 11 <= k <= 19:
    word = "грибов"
else:
    last_digit = k % 10
    if last_digit == 1:
        word = "гриб"
    elif 2 <= last_digit <= 4:
        word = "гриба"
    else:
        word = "грибов"
print(f"мы нашли {k} {word} в лесу")
