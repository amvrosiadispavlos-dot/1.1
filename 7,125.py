y = list(map(float, input("Введите 15 вещественных чисел по возрастанию через пробел: ").split()[:15]))
n = float(input("Введите число n (y₁ < n < y₁₅): "))
sum_less = 0
for val in y:
    if val < n:
        sum_less += val
    else:
        break  
print(f"а) Сумма чисел, меньших {n}: {sum_less}")
left_index = -1
right_index = -1
for i in range(len(y) - 1):
    if y[i] < n < y[i+1]:
        left_index = i + 1
        right_index = i + 2
        break
if left_index != -1:
    print(f"б) n находится между элементами {left_index} ({y[left_index-1]}) и {right_index} ({y[right_index-1]})")
else:
    print("б) n не находится между элементами последовательности (нарушены условия задачи).")
