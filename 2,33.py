x = int(input("Возраст Тани (лет): "))
y = int(input("Возраст Мити (лет): "))
average_age = (x + y) / 2
diff_tanya = x - average_age
diff_mitia = y - average_age
print(f"Средний возраст: {average_age:.1f} лет")
print(f"Отклонение возраста Тани: {diff_tanya:.1f} лет")
print(f"Отклонение возраста Мити: {diff_mitia:.1f} лет")
