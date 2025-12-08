n = input("Введите натуральное число: ")
mono_increasing = True
for i in range(len(n)-1):
    if n[i] >= n[i+1]:
        mono_increasing = False
        break
print(f"Цифры образуют монотонно возрастающую последовательность: {mono_increasing}")
