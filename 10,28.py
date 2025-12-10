import random

def monte_carlo_pi(accuracy=0.0001):
    n = 0
    inside = 0
    pi_estimate = 0
    prev_estimate = 0
    
    while True:
        # Генерируем точку в квадрате [-1, 1] x [-1, 1]
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        
        n += 1
        if x**2 + y**2 <= 1:
            inside += 1
        
        # Новое приближение
        pi_estimate = 4 * inside / n
        
        # Проверка точности
        if n >= 100 and abs(pi_estimate - prev_estimate) < accuracy:
            break
        
        if n % 10000 == 0:
            prev_estimate = pi_estimate
    
    return pi_estimate, n

pi_approx, iterations = monte_carlo_pi()
print(f"Приближение π: {pi_approx:.6f}")
print(f"Итераций: {iterations}")
print(f"Разница с math.pi: {abs(pi_approx - math.pi):.6f}")
