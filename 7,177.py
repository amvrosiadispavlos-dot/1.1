seq = [5, 8, 3, 8, 2, 8, 7, 8, 1] 
max_val = 8
count_max = seq.count(max_val)
print(f"Исходное количество максимальных элементов ({max_val}): {count_max}")
A1 = 0
new_seq1 = seq + [A1]
new_count1 = new_seq1.count(max_val)
print(f"После дописывания {A1}: максимальных элементов = {new_count1}")
A2 = 8
new_seq2 = seq + [A2]
new_count2 = new_seq2.count(max_val)
print(f"После дописывания {A2}: максимальных элементов = {new_count2}")
