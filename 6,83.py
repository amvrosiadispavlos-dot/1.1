n = input("Введите натуральное число: ")
if len(n) <= 1:
    print("Число слишком короткое для определения монотонности")
else:
    increasing = all(n[i] < n[i+1] for i in range(len(n)-1))
    decreasing = all(n[i] > n[i+1] for i in range(len(n)-1))
    monotonic = increasing or decreasing
    print(f"Цифры образуют монотонную последовательность (возрастающую или убывающую): {monotonic}")
