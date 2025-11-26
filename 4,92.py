t = float(input("t (минуты с начала часа) = "))
pos = t % 6
if pos < 3:
    print("зелёный")
elif pos < 4:
    print("жёлтый")
else:
    print("красный")
