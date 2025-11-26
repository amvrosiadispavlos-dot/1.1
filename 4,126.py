a = int(input("a = "))
b = int(input("b = "))
if b % a == 0:
    print("a является делителем b")
elif a % b == 0:
    print("b является делителем a")
else:
    print("ни одно из чисел не является делителем другого")
