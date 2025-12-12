import random
heights = [random.randint(150, 180) for _ in range(22)]
for i in range(11):
    heights[i] = -heights[i]
boys = [-h for h in heights if h < 0]
girls = [h for h in heights if h > 0]
avg_boy = sum(boys) / len(boys) if boys else 0
avg_girl = sum(girls) / len(girls) if girls else 0
print(f"Средний рост мальчиков: {avg_boy:.1f}")
print(f"Средний рост девочек: {avg_girl:.1f}")
