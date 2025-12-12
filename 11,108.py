arr = [10, -4, 12, 56, -4, -89]
sign_changes = 0
for i in range(1, len(arr)):
    if (arr[i-1] > 0 and arr[i] < 0) or (arr[i-1] < 0 and arr[i] > 0):
        sign_changes += 1
print(f"Массив: {arr}")
print(f"Число смен знака: {sign_changes}")
