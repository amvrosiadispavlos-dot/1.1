powers = list(map(int, input("Введите мощности 30 моделей через пробел: ").split()[:30]))
has_power_gt_200 = any(p > 200 for p in powers)
print(f"Есть модель мощнее 200 л.с.: {has_power_gt_200}")
