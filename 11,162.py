import random
heights = sorted([random.randint(150, 190) for _ in range(25)], reverse=True)
print("Рост учеников (по убыванию):", heights)

case = int(input("Выберите случай (1 или 2): "))
if case == 1:
    i1 = int(input("Введите первый номер выбывшего (1-25): "))
    i2 = int(input("Введите второй номер выбывшего (1-25): "))
    indices = sorted([i1-1, i2-1], reverse=True)  # удаляем с конца
    for idx in indices:
        for i in range(idx, len(heights)-1):
            heights[i] = heights[i+1]
        heights[-1] = 0
    print("Новый массив:", heights[:-2])  # два последних теперь 0
elif case == 2:
    h1 = int(input("Введите рост первого выбывшего: "))
    h2 = int(input("Введите рост второго выбывшего: "))
    if h1 in heights and h2 in heights:
        indices = [heights.index(h1), heights.index(h2)]
        indices.sort(reverse=True)
        for idx in indices:
            for i in range(idx, len(heights)-1):
                heights[i] = heights[i+1]
            heights[-1] = 0
        print("Новый массив:", heights[:-2])
    else:
        print("Одного или обоих учеников с таким ростом нет")
