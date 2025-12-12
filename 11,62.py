import random
february_precipitation = [random.randint(0, 10) for _ in range(28)]
sum_even_days = sum(february_precipitation[i] for i in range(1, 28, 2)) 
print(f"Осадки по дням февраля: {february_precipitation}")
print(f"Сумма осадков по четным числам: {sum_even_days}")
