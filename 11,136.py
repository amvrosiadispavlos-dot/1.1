import random
wind_directions = [random.randint(1, 8) for _ in range(365)]
from collections import Counter
wind_counts = Counter(wind_directions)
most_common = wind_counts.most_common(1)[0][0]
direction_names = {
    1: "север", 2: "юг", 3: "восток", 4: "запад",
    5: "северо-запад", 6: "северо-восток", 
    7: "юго-запад", 8: "юго-восток"
}
print(f"Наиболее частый ветер: {direction_names[most_common]}")
print("Жилой комплекс следует расположить с противоположной стороны от комбината")
