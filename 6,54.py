n = input("Введите натуральное число: ")
count_0 = 0
count_9 = 0
for digit in n:
    if digit == '0':
        count_0 += 1
    if digit == '9':
        count_9 += 1
if count_0 > count_9:
    print("Чаще встречается 0")
elif count_9 > count_0:
    print("Чаще встречается 9")
else:
    print("0 и 9 встречаются одинаково часто или отсутствуют")
