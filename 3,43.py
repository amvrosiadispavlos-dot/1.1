a2 = int(input("a₂ (десятки первого): "))
a1 = int(input("a₁ (единицы первого): "))
b2 = int(input("b₂ (десятки второго): "))
b1 = int(input("b₁ (единицы второго): "))
sum_units = a1 + b1
r1 = sum_units % 10
carry1 = sum_units // 10
sum_tens = a2 + b2 + carry1
r2 = sum_tens % 10
print(f"Цифры результата: десятки = {r2}, единицы = {r1}")
