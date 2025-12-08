correct_password = 1234  
while True:
    password = int(input("Введите пароль (целое число): "))
    if password == correct_password:
        print("Добро пожаловать!")
        break
    else:
        print("Неверный пароль. Попробуйте снова.")
