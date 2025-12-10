import random
print("Чет (введите 2) или нечет (введите 1)?")
user = int(input())
computer = random.choice([1, 2])
print(f"Компьютер выбрал: {computer}")
if user == computer:
    print("Вы угадали!")
else:
    print("Вы не угадали.")

import random
n = int(input("Сколько раз играем? "))
user_score = 0
comp_score = 0

for _ in range(n):
    print("\nЧет (2) или нечет (1)?")
    user = int(input())
    computer = random.choice([1, 2])
    print(f"Компьютер: {computer}")
    if user == computer:
        user_score += 1
    else:
        comp_score += 1

print(f"\nСчет {user_score}:{comp_score}", end=" ")
if user_score > comp_score:
    print("в вашу пользу. Вы выиграли!")
elif user_score < comp_score:
    print("в пользу компьютера. Вы проиграли!")
else:
    print("ничья!")
import random
user_wins = 0
comp_wins = 0

while True:
    print("\nЧет (2) или нечет (1)?")
    user = int(input())
    computer = random.choice([1, 2])
    print(f"Компьютер: {computer}")
    if user == computer:
        user_wins += 1
        print("Верно!")
    else:
        comp_wins += 1
        print("Неверно!")
    
    again = input("Продолжить еще раз? (да/нет): ").lower()
    if 'н' in again:
        break

print(f"\nИтог: верных ответов {user_wins}, неверных {comp_wins}")
