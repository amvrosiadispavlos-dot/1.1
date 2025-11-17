h = int(input("Часы (0 < h ≤ 12): "))
m = int(input("Минуты (0 ≤ m ≤ 59): "))
t_match = (30 * h - 5.5 * m) / 5.5
if t_match < 0:
    t_match += 720 / 11
t_perp1 = (30 * h - 5.5 * m - 90) / 5.5
t_perp2 = (30 * h - 5.5 * m + 90) / 5.5
t_perp = min(t for t in [t_perp1, t_perp2, t_perp1 + 720/11, t_perp2 + 720/11] if t > 0)
print(f"а) До совпадения: {t_match:.2f} минут")
print(f"б) До перпендикулярного положения: {t_perp:.2f} минут")
