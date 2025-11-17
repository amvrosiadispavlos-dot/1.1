N = int(input("Введите количество школьников: "))
k = int(input("Введите количество яблок: "))
apples_per_student = k // N
apples_in_basket = k % N
print("Каждому школьнику достанется:", apples_per_student)
print("В корзинке останется:", apples_in_basket)
