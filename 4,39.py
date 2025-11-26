t = float(input("t (минуты с начала часа) = "))
pos = t % 5
if pos < 3:
    print("зелёный")
else:
    print("красный")
