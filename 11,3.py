import random

# а)
arr_a = [random.random() for _ in range(15)]
print("а) [0, 1):", arr_a)

# б)
arr_b = [random.uniform(22, 23) for _ in range(15)]
print("б) [22, 23):", arr_b)

# в)
arr_c = [random.uniform(0, 10) for _ in range(15)]
print("в) [0, 10):", arr_c)

# г)
arr_d = [random.uniform(-50, 50) for _ in range(15)]
print("г) [-50, 50):", arr_d)

# д)
arr_e = [random.randint(0, 10) for _ in range(15)]
print("д) [0, 10]:", arr_e)
