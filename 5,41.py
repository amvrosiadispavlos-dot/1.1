num = int(input("Число: "))
n = int(input("n (количество последних цифр): "))
product = 1
sum_digits = 0
for _ in range(n):
    digit = num % 10 
    product *= digit
    sum_digits += digit
    num //= 10  
print("Произведение последних", n, "цифр:", product)
print("Сумма последних", n, "цифр:", sum_digits)
