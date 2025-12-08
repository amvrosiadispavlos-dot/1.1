numbers = list(map(int, input("Введите набор целых чисел через пробел: ").split()))
has_even = any(x % 2 == 0 for x in numbers)
print(f"В наборе есть хотя бы одно чётное число: {has_even}")
