exchange_rate = float(input("Курс доллара (рублей за 1 доллар): "))
print("Доллары | Рубли")
print("-" * 16)
for dollars in range(1, 21):
    rubles = dollars * exchange_rate
    print(f"{dollars:2d}      | {rubles:6.2f}")
