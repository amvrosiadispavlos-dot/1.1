n = input("Введите натуральное число: ")
a = input("Введите цифру a для удаления: ")
reversed_n = ""
without_a = ""
swapped = ""
doubled = n + n
with_two = '2' + n + '2'
for i, digit in enumerate(n):
    reversed_n = digit + reversed_n  
    if digit != a:
        without_a += digit
    if i == 0:
        first = digit
    if i == len(n) - 1:
        last = digit
if len(n) == 1:
    swapped = n
else:
    swapped = last + n[1:-1] + first
print(f"а) Число справа налево: {reversed_n}")
print(f"б) С двойкой в начале и конце: {with_two}")
print(f"в) Без цифры {a}: {without_a if without_a else '0'}")
print(f"г) С переставленными первой и последней цифрами: {swapped}")
print(f"д) Исходное + исходное: {doubled}")
