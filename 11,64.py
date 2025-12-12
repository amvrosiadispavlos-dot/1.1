arr = [3, -5, 8, -2, 10, -7]
positive_sum = sum(x for x in arr if x > 0)
negative_sum = sum(x for x in arr if x < 0)
if negative_sum != 0:
    quotient = positive_sum / abs(negative_sum)
    print(f"Частное: {quotient:.2f}")
else:
    print("Сумма отрицательных равна 0, деление невозможно")
