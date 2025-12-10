import random
a = random.randint(1, 9)
b = random.randint(1, 9)
answer = int(input(f"Чему равно произведение {a}×{b}? "))
if answer == a * b:
    print("Правильно!")
else:
    print(f"Неправильно. Правильный ответ: {a*b}")

import random
correct = 0
for _ in range(20):
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    answer = int(input(f"Чему равно произведение {a}×{b}? "))
    if answer == a * b:
        correct += 1
        print("Правильно!")
    else:
        print(f"Неправильно. Правильный ответ: {a*b}")
print(f"\nПравильных ответов: {correct}, неправильных: {20-correct}")

import random
while True:
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    answer = int(input(f"Чему равно произведение {a}×{b}? (0 для выхода) "))
    if answer == 0:
        break
    if answer == a * b:
        print("Правильно!")
    else:
        print(f"Неправильно. Правильный ответ: {a*b}")
