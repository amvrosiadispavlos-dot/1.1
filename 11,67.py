import random
residents = [random.randint(10, 50) for _ in range(20)]
odd_side = sum(residents[i] for i in range(0, 20, 2))
even_side = sum(residents[i] for i in range(1, 20, 2))
print(f"Жителей на нечетной стороне: {odd_side}")
print(f"Жителей на четной стороне: {even_side}")
if odd_side > even_side:
    print("Больше жителей на нечетной стороне")
elif even_side > odd_side:
    print("Больше жителей на четной стороне")
else:
    print("Количество жителей одинаково")
