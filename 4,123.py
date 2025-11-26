points = int(input("Очки команды (0, 1 или 3) = "))
if points == 3:
    result = "выигрыш"
elif points == 1:
    result = "ничья"
else:  # points == 0
    result = "проигрыш"
print("Результат игры:", result)
