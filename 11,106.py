arr = [2, 4, 6, 8, 10, 4]
from collections import Counter
counts = Counter(arr)
exactly_two = any(count == 2 for count in counts.values())
print("Имеются только два одинаковых элемента:", exactly_two)
