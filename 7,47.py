print("Введите стоимости товаров через пробел (закончите ввод любым нечисловым символом или пустой строкой):")
prices = []
while True:
    try:
        price = float(input())
        prices.append(price)
    except:
        break
total_expensive = sum(p for p in prices if p > 1000)
print(f"Общая стоимость товаров дороже 1000 руб.: {total_expensive}")
