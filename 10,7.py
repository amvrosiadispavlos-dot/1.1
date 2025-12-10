import random

# а)
a = random.randint(0, 1)
while True:
    b = random.randint(0, 2)
    if b != a:
        break
print(f"а) a = {a}, b = {b}")

# б)
a = random.randint(1, 2)
while True:
    b = random.randint(0, 2)
    if b != a:
        break
while True:
    c = random.randint(1, 3)
    if c != a and c != b:
        break
print(f"б) a = {a}, b = {b}, c = {c}")

# в)
numbers = [2]*7 + [3]*8
random.shuffle(numbers)
print("в) 15 чисел (7 двоек, 8 троек):")
print(' '.join(map(str, numbers)))
