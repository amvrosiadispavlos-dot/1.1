import random
prices = [random.randint(100, 1000) for _ in range(20)]
print("Исходные цены товаров:", prices)
n = int(input("Введите номер товара, который снимается с продажи (1-20): "))
if 1 <= n <= 20:
    for i in range(n-1, len(prices)-1):
        prices[i] = prices[i+1]
    prices[-1] = 0
    print("Новый массив цен:", prices[:19])  # последний элемент 0 не выводим
else:
    print("Неверный номер товара")
