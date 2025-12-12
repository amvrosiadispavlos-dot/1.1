arr = [3, 7, 9, 5, 9, 2, 8]
print("Исходный массив:", arr)
num1 = 100
num2 = 200
max_val = max(arr)
max_index = arr.index(max_val) 

arr.append(0)
for i in range(len(arr)-1, max_index+1, -1):
    arr[i] = arr[i-1]
arr[max_index+1] = num1

arr.append(0)
for i in range(len(arr)-1, max_index, -1):
    arr[i] = arr[i-1]
arr[max_index] = num2

print("После вставки двух чисел:", arr)
