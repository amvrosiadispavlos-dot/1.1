a = int(input("a (длинная сторона стола) = "))
b = int(input("b (короткая сторона стола) = "))
c = int(input("c (самый длинный размер кости) = "))
d = int(input("d (средний размер кости) = "))
e = int(input("e (самый короткий размер кости) = "))
count1 = (a // c) * (b // d) if c <= a and d <= b else 0
count2 = (a // d) * (b // c) if d <= a and c <= b else 0
max1 = max(count1, count2)
count3 = (a // c) * (b // e) if c <= a and e <= b else 0
count4 = (a // e) * (b // c) if e <= a and c <= b else 0
max2 = max(count3, count4)
count5 = (a // d) * (b // e) if d <= a and e <= b else 0
count6 = (a // e) * (b // d) if e <= a and d <= b else 0
max3 = max(count5, count6)
max_count = max(max1, max2, max3)
print("Максимальное количество костей:", max_count)
