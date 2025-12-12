heights = [8848, 8611, 8586, 8516, 8485, 8201, 8167, 8163, 8126, 8091]
heights = heights[:10] + [0]  
new_height = 8321  
position = 3 
for i in range(len(heights)-1, position, -1):
    heights[i] = heights[i-1]
heights[position] = new_height
print("Новый массив высот:", heights)
