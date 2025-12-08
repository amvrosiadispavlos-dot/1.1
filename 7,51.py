print("Введите последовательность целых чисел через пробел:")
numbers = list(map(int, input().split()))
sum_odd_start = 0
for num in numbers:
    if num % 2 == 1: 
        sum_odd_start += num
    else:
        break  
print(f"Сумма первых подряд идущих нечётных чисел: {sum_odd_start}")
