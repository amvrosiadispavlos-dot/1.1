heights = [185, 182, 180, 178, 175, 173, 170, 168, 165, 163, 160, 158, 155, 153, 150]
new_height = 176
place = sum(1 for h in heights if h > new_height) + 1
print(f"Новый ученик займет {place}-е место")
