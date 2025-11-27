import math
n = int(input("n = "))
total_sum = 0
sin_sum = 0
for i in range(1, n + 1):
    sin_sum += math.sin(i)
    total_sum += 1 / sin_sum
print("а) Результат:", total_sum)
import math
n = int(input("n = "))
result = math.sqrt(2)
for _ in range(1, n):
    result = math.sqrt(2 + result)
print("б) Результат:", result)
import math
n = int(input("n = "))
total = 0
cos_sum = 0
for i in range(1, n + 1):
    cos_sum += math.cos(i)
    total += cos_sum
print("в) Результат:", total)
import math
n = int(input("n = "))
total = 0
sin_sum = 0
for i in range(1, 2 * n + 1):
    sin_sum += math.sin(i)
    total += sin_sum
print("г) Результат:", total)
