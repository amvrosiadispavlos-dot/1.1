a1, a2, a3 = float(input("a1 = ")), float(input("a2 = ")), float(input("a3 = "))
b1, b2, b3 = float(input("b1 = ")), float(input("b2 = ")), float(input("b3 = "))
a_sorted = sorted([a1, a2, a3])
b_sorted = sorted([b1, b2, b3])
fits = (b_sorted[0] <= a_sorted[0] and 
        b_sorted[1] <= a_sorted[1] and 
        b_sorted[2] <= a_sorted[2])
print("Коробка помещается в чемодан:", fits)
print("Можно сэкономить:", fits)
