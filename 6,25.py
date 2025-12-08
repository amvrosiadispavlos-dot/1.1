n = int(input("n = "))
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        print("Наименьший делитель:", i)
        break
else:
    print("Наименьший делитель:", n)  # если число простое
