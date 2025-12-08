n = int(input("Введите количество людей: "))
masses = list(map(float, input("Введите массу каждого через пробел: ").split()[:n]))
max_mass = max(masses)
min_mass = min(masses)
cond = max_mass > 2 * min_mass
print(f"Самый тяжёлый: {max_mass} кг")
print(f"Самый лёгкий: {min_mass} кг")
print(f"Самый тяжёлый превышает самого лёгкого более чем в 2 раза: {cond}")
