k = int(input("Введите k (1 ≤ k ≤ 150): "))
number_index = (k - 1) // 3
three_digit_number = 101 + number_index
position_in_number = (k - 1) % 3
if position_in_number == 0:
    digit = three_digit_number // 100
elif position_in_number == 1:
    digit = (three_digit_number // 10) % 10
else:
    digit = three_digit_number % 10
print(f"{k}-я цифра: {digit}")
if k % 3 == 0:
    print(f"(k кратно 3) {k}-я цифра: {three_digit_number % 10}")
elif k % 3 == 1:
    print(f"(k = 1,4,7,...) {k}-я цифра: {three_digit_number // 100}")
else:
    print(f"(k = 2,5,8,...) {k}-я цифра: {(three_digit_number // 10) % 10}")
