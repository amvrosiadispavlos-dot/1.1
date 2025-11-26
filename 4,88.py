y_b = int(input("Год рождения: "))
m_b = int(input("Месяц рождения: "))
y_t = int(input("Текущий год: "))
m_t = int(input("Текущий месяц: "))
total_months = (y_t - y_b) * 12 + (m_t - m_b)
years = total_months // 12
months = total_months % 12
print(f"Возраст: {years} лет {months} месяцев")
