a3 = int(input("a₃ (сотни трехзначного): "))
a2 = int(input("a₂ (десятки трехзначного): "))
a1 = int(input("a₁ (единицы трехзначного): "))
b2 = int(input("b₂ (десятки двузначного): "))
b1 = int(input("b₁ (единицы двузначного): "))
sum_units = a1 + b1
r1 = sum_units % 10
carry1 = sum_units // 10
sum_tens = a2 + b2 + carry1
r2 = sum_tens % 10
carry2 = sum_tens // 10
r3 = a3 + carry2
print(f"Цифры результата: сотни = {r3}, десятки = {r2}, единицы = {r1}")
