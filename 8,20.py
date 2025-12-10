# a)
print("a)")
for i in range(4):
    print("8 8 8")

print()

# b)
print("b)")
for i in range(1, 9):
    print(f"{i*10} {i*10} {i*10} {i*10}")

print()

# c)
print("c)")
for i in range(1, 9):
    print(f"{i*10+2} {i*10+2} {i*10+2} {i*10+2}")

print()

# d)
print("d)")
for i in range(5):
    for j in range(2, 21):
        print(j, end=' ')
    print()

print()

# e)
print("e)")
for i in range(5):
    for j in range(15, 2, -1):
        print(j, end=' ')
    print()

print()

# f)
print("f)")
for i in range(5):
    for j in range(5):
        print("0", end=' ')
    print()

print()

# g)
print("g)")
for i in range(5):
    for j in range(8, 0, -1):
        print(j, end=' ')
    print()

print()

# h)
print("h)")
for i in range(1, 9):
    for j in range(i+1, i+9):
        print(j, end=' ')
    print()

print()

# i)
print("i)")
for i in range(4):
    for j in range(2, 10):
        print(j, end=' ')
    print()

print()

# к)
print("к)")
for i in range(3, 7):
    for j in range(i):
        print(i, end=' ')
    print()

print()

# л)
print("л)")
for i in range(21, 26):
    for j in range(i-20):
        print(i, end=' ')
    print()

print()

# м)
print("м)")
for i in range(1, 6):
    for j in range(11 - i):
        print(i, end=' ')
    print()

for i in range(1, 6):
    for j in range(i):
        print(i*10, end=' ')
    print()

print()

# о)
print("о)")
for i in range(5, 10):
    for j in range(10 - i):
        print(i, end=' ')
    print()

for i in range(1, 6):
    for j in range(6 - i):
        print(i*5, end=' ')
    print()

print()

# р)
print("р)")
for i in range(0, 7):
    for j in range(1, 6):
        print(f"1{i}{j}", end=' ')
    print()

print()

# с)
print("с)")
for i in range(5, 0, -1):
    for j in range(1, 5):
        if j == 4:
            print(f"{i*10+8}", end=' ')
        else:
            print(f"{i*10+j}", end=' ')
    print()
