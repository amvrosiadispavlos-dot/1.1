a = int(input("Введите a: "))
b = int(input("Введите b: "))
max_div_count = 0
results = []
for num in range(a, b+1):
    count = sum(1 for i in range(1, num+1) if num % i == 0)
    if count > max_div_count:
        max_div_count = count
        results = [num]
    elif count == max_div_count:
        results.append(num)
if results:
    print(f"Наибольшее: {max(results)}")
    print(f"Наименьшее: {min(results)}")
else:
    print("Нет чисел в интервале")
