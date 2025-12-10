import random

values = [0, 1, 2, 3, 4, 5, 6]
all_bones = [(i, j) for i in values for j in range(i, 7)]

bone1, bone2 = random.sample(all_bones, 2)
print(f"Кость 1: {bone1[0]}-{bone1[1]}")
print(f"Кость 2: {bone2[0]}-{bone2[1]}")

if (bone1[0] in bone2 or bone1[1] in bone2):
    print("Кости можно приставить друг к другу")
else:
    print("Кости нельзя приставить друг к другу")
