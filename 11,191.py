arr = [1, 2, 0, 4, 5, 0, 7, 8]
first_zero_index = arr.index(0)
print(f"Все элементы, кроме первого нуля: {arr[:first_zero_index] + arr[first_zero_index+1:]}")

arr = [1, 2, 0, 4, 5, 0, 7, 8]
last_zero_index = len(arr) - 1 - arr[::-1].index(0)
print(f"Все элементы, кроме последнего нуля: {arr[:last_zero_index] + arr[last_zero_index+1:]}")
