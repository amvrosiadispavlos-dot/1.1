arr = [12.5, 8.3, 15.7, 9.2, 20.1, 7.5]
max_val = max(arr)
min_val = min(arr)
condition_a = (max_val - min_val) <= 25
condition_b = min_val < max_val / 2
print(f"a) Макс превышает мин не более чем на 25: {condition_a}")
print(f"б) Мин меньше макс более чем в 2 раза: {condition_b}")
