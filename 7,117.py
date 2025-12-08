heights = list(map(float, input("Введите рост учеников (мальчики - отрицательные) через пробел: ").split()))
boys = [h for h in heights if h < 0]
girls = [h for h in heights if h >= 0]
avg_boys = -sum(boys) / len(boys) if boys else 0 
avg_girls = sum(girls) / len(girls) if girls else 0
cond = avg_boys > avg_girls + 10
print(f"Средний рост мальчиков: {avg_boys:.2f} см")
print(f"Средний рост девочек: {avg_girls:.2f} см")
print(f"Рост мальчиков превышает рост девочек более чем на 10 см: {cond}")
