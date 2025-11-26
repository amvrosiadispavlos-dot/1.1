from datetime import date
y_b = int(input("Год рождения: "))
m_b = int(input("Месяц рождения: "))
d_b = int(input("День рождения: "))
y_t = int(input("Текущий год: "))
m_t = int(input("Текущий месяц: "))
d_t = int(input("Текущий день: "))
birth = date(y_b, m_b, d_b)
today = date(y_t, m_t, d_t)
age = today.year - birth.year
if (today.month, today.day) < (birth.month, birth.day):
    age -= 1
print(f"Возраст: {age} полных лет")
