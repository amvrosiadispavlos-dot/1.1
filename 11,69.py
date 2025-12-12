arr = [2, 4, 6, 2, 8, 2]
last = arr[-1]
count_diff = sum(1 for x in arr if x != last)
a = 3
count_multiple = sum(1 for x in arr if x % a == 0)
print(f"а) Элементов, отличных от последнего ({last}): {count_diff}")
print(f"б) Элементов, кратных {a}: {count_multiple}")
