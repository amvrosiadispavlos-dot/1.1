def spiral_fence_length(a, b):
    length = 0
    while a > 1 and b > 1:
        length += (a + b - 2) * 2 - 2  
        a -= 2
        b -= 2
    if a == 1 and b > 1:
        length += b - 1
    elif b == 1 and a > 1:
        length += a - 1
    return length
a = int(input("Введите длину лужайки a: "))
b = int(input("Введите ширину лужайки b: "))
print(f"Длина ограждения для лужайки {a}×{b}: {spiral_fence_length(a, b)}")
