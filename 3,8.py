ticket_number = int(input("Введите номер билета: "))
seat_index = ticket_number - 1642
if 1 <= seat_index <= 300:
    row = (seat_index - 1) // 15 + 1
    print("Билет находится в ряду №", row)
else:
    print("Такого билета не существует.")
