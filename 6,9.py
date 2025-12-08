while True:
    num = int(input("Введите чётное число: "))
    if num % 2 == 0:
        print("Спасибо!")
        break
    else:
        print("Ошибка: число нечётное. Попробуйте снова.")
