population = int(input("Введите количество жителей: "))
area = float(input("Введите площадь территории (км²): "))

population_density = population / area
print(f"Плотность населения: {population_density:.2f} чел/км²")
