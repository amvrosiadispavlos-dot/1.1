import random
feb_precip = [random.randint(0, 10) for _ in range(28)]
even_sum = sum(feb_precip[i] for i in range(1, 28, 2))
odd_sum = sum(feb_precip[i] for i in range(0, 28, 2))
print(f"Сумма по четным: {even_sum}")
print(f"Сумма по нечетным: {odd_sum}")
print(f"По четным больше: {even_sum > odd_sum}")
