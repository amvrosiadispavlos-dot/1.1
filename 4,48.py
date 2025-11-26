m = int(input("m = "))
n = int(input("n = "))
if (m != 0 and n % m == 0) or (n != 0 and m % n == 0):
    print("Одно является делителем другого")
else:
    print("Ни одно не является делителем другого")
