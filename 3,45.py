k = int(input("Введите k (1 ≤ k ≤ 180): "))
pair_number = (k - 1) // 2 + 10
two_digit_number = pair_number
position_in_pair = (k - 1) % 2 
if position_in_pair == 0:
    k_digit = two_digit_number // 10 
else:
    k_digit = two_digit_number % 10  
print(f"а) Номер пары цифр: {pair_number}")
print(f"б) Двузначное число: {two_digit_number}")
print(f"в) {k}-я цифра: {k_digit}")
if k % 2 == 0:
    print(f"   (k четное) {k}-я цифра: {two_digit_number % 10}")
else:
    print(f"   (k нечетное) {k}-я цифра: {two_digit_number // 10}")
