heights = list(map(int, input("Введите рост 12 юношей (см) через пробел: ").split()[:12]))
count_less_165 = sum(1 for h in heights if h < 165)
print(f"Количество юношей ростом менее 165 см: {count_less_165}")
