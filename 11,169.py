heights = sorted([random.randint(170, 190) for _ in range(15)], reverse=True)
print("Рост учеников (по убыванию):", heights)

case = int(input("Выберите случай (1 или 2): "))
if case == 1:
    position = int(input("Введите порядковый номер нового ученика (1-16): "))
    new_height = int(input("Введите рост нового ученика: "))
    heights.append(0)
    for i in range(len(heights)-1, position-1, -1):
        heights[i] = heights[i-1]
    heights[position-1] = new_height
    print("Новый массив:", heights)
elif case == 2:
    new_height = int(input("Введите рост нового ученика: "))
    heights.append(0)
    pos = 0
    while pos < len(heights)-1 and heights[pos] > new_height:
        pos += 1
    for i in range(len(heights)-1, pos, -1):
        heights[i] = heights[i-1]
    heights[pos] = new_height
    print("Новый массив:", heights)
