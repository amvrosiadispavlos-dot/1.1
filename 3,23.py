num = int(input("Введите трехзначное число: "))
last_digit = num % 10
first_two = num // 10
new_num = last_digit * 100 + first_two
print("Число после перестановки:", new_num)
