import random

answers = []
for i in range(20):
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    answer = int(input(f"{i+1}. Чему равно произведение {a} на {b}? "))
    answers.append(answer)

print("\nВаши ответы:", answers)
