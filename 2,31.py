price_sweets = float(input("Стоимость 1 кг конфет: "))
price_cookies = float(input("Стоимость 1 кг печенья: "))
price_apples = float(input("Стоимость 1 кг яблок: "))
kg_sweets = float(input("Купили кг конфет: "))
kg_cookies = float(input("Купили кг печенья: "))
kg_apples = float(input("Купили кг яблок: "))
total_cost = (price_sweets * kg_sweets + 
              price_cookies * kg_cookies + 
              price_apples * kg_apples)
print(f"Общая стоимость покупки: {total_cost:.2f}")
