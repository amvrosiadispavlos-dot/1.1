print("Введите число жителей в каждом доме (последовательно):")
residents = list(map(int, input().split()))
sum_odd = sum(residents[i] for i in range(0, len(residents), 2))  
sum_even = sum(residents[i] for i in range(1, len(residents), 2)) 
if sum_odd > sum_even:
    print("Больше жителей на стороне с нечётными номерами домов")
elif sum_even > sum_odd:
    print("Больше жителей на стороне с чётными номерами домов")
else:
    print("На обеих сторонах улицы одинаковое число жителей")
