arr = [1, 3, 5, 7, 9, 3]
from collections import Counter
counts = Counter(arr)
duplicates = [num for num, count in counts.items() if count == 2]
print("Два одинаковых элемента:", duplicates)
