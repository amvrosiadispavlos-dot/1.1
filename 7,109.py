numbers = list(map(int, input("Введите 12 целых чисел через пробел: ").split()[:12]))
even = [x for x in numbers if x % 2 == 0]
odd = [x for x in numbers if x % 2 != 0]
avg_even = sum(even) / len(even) if even else 0
avg_odd = sum(odd) / len(odd) if odd else 0
print(f"Среднее чётных: {avg_even}")
print(f"Среднее нечётных: {avg_odd}")
