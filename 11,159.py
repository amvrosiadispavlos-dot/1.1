import random
heights = sorted([random.randint(150, 190) for _ in range(25)], reverse=True)
print("Рост учеников (по убыванию):", heights)

case = int(input("Выберите случай (1 или 2): "))
if case == 1:
    index = int(input("Введите порядковый номер выбывшего (1-25): "))
    if 1 <= index <= 25:
        for i in range(index-1, len(heights)-1):
            heights[i] = heights[i+1]
        heights[-1] = 0
        print("Новый массив (последний 0 игнорируем):", heights[:-1])
elif case == 2:
    height = int(input("Введите рост выбывшего ученика: "))
    if height in heights:
        index = heights.index(height)
        for i in range(index, len(heights)-1):
            heights[i] = heights[i+1]
        heights[-1] = 0
        print("Новый массив (последний 0 игнорируем):", heights[:-1])
    else:
        print("Ученика с таким ростом нет в классе")
