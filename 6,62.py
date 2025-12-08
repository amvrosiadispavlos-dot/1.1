n = input("Введите натуральное число: ")
reversed_n = n[::-1]
print(f"а) Число справа налево: {reversed_n}")
with_two = '2' + n + '2'
print(f"б) С двойкой в начале и конце: {with_two}")
a = input("Введите цифру a для удаления: ")
without_a = ''
for digit in n:
    if digit != a:
        without_a += digit
print(f"в) Без цифры {a}: {without_a if without_a else '0'}")
if len(n) == 1:
    swapped = n
else:
    swapped = n[-1] + n[1:-1] + n[0]
print(f"г) С переставленными первой и последней цифрами: {swapped}")
doubled = n + n
print(f"д) Исходное + исходное: {doubled}")
