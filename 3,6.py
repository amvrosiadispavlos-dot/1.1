seat = int(input("Введите номер места: "))
compartment = (seat - 1) // 4 + 1
print("Место находится в купе №", compartment)
