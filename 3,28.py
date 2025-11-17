num = int(input("Введите четырехзначное число: "))
thousands = num // 1000
hundreds = (num // 100) % 10
tens = (num // 10) % 10
units = num % 10
reversed_num = units * 1000 + tens * 100 + hundreds * 10 + thousands
print("а) Число справа налево:", reversed_num)
new_num_b = hundreds * 1000 + thousands * 100 + units * 10 + tens
print("б) После перестановки 1-2 и 3-4 цифр:", new_num_b)
new_num_c = thousands * 1000 + tens * 100 + hundreds * 10 + units
print("в) После перестановки 2-3 цифр:", new_num_c)
new_num_d1 = tens * 1000 + units * 100 + thousands * 10 + hundreds
print("г) Способ 1 (с выделением цифр):", new_num_d1)
last_two = num % 100  
first_two = num // 100 
new_num_d2 = last_two * 100 + first_two
print("   Способ 2 (без выделения цифр):", new_num_d2)
