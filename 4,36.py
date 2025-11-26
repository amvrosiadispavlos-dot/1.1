n = int(input("Введите натуральное число: "))
last_digit = n % 10
a_ans = (last_digit % 2 == 0)
print("а) Заканчивается чётной цифрой:", a_ans)
b_ans = (last_digit % 2 == 1)
print("б) Заканчивается нечётной цифрой:", b_ans)
