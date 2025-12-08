n = int(input("Введите количество сотрудников: "))
salaries = list(map(float, input("Введите зарплаты через пробел: ").split()[:n]))
print("Общая сумма выплат:", sum(salaries))
