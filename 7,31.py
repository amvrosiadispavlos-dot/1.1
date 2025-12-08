print("Введите неотрицательные целые числа, оканчивающиеся отрицательным:")
seq = []
while True:
    num = int(input())
    if num < 0:
        break
    seq.append(num)
if seq:
    average = sum(seq) / len(seq)
    print("Среднее арифметическое:", average)
else:
    print("Последовательность пуста (нет неотрицательных чисел)")
