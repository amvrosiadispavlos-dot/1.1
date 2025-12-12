import random
scores = [random.randint(4, 6) for _ in range(18)]
compulsory = scores[:6]
free = scores[6:]
avg_compulsory = sum(compulsory) / len(compulsory)
avg_free = sum(free) / len(free)
print(f"Обязательная программа: {compulsory}, среднее: {avg_compulsory:.2f}")
print(f"Произвольная программа: {free}, среднее: {avg_free:.2f}")
if avg_compulsory > avg_free:
    print("Лучший результат в обязательной программе")
elif avg_free > avg_compulsory:
    print("Лучший результат в произвольной программе")
else:
    print("Результаты равны")
