print("Введите стоимости предметов первого набора (8 чисел через пробел):")
prices1 = list(map(float, input().split()[:8]))
print("Введите стоимости предметов второго набора (8 чисел через пробел):")
prices2 = list(map(float, input().split()[:8]))
total1 = sum(prices1)
total2 = sum(prices2)
if total1 < total2:
    print(f"Первый набор дешевле: {total1} < {total2}")
elif total2 < total1:
    print(f"Второй набор дешевле: {total2} < {total1}")
else:
    print(f"Стоимость наборов одинакова: {total1} = {total2}")
