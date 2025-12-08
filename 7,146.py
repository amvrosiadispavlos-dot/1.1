n = int(input("Введите количество людей: "))
heights = list(map(float, input("Введите рост каждого через пробел: ").split()[:n]))
max_height = max(heights)
min_height = min(heights)
difference = max_height - min_height
print(f"Самый высокий: {max_height} см")
print(f"Самый низкий: {min_height} см")
print(f"Разница: {difference:.2f} см")
