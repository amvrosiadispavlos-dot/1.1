n = 20 
min_current = float('inf')
min_res_index = -1
for i in range(n):
    voltage = float(input(f"Напряжение на сопротивлении {i+1} (В): "))
    resistance = float(input(f"Сопротивление {i+1} (Ом): "))
    current = voltage / resistance if resistance > 0 else float('inf')
    if current < min_current:
        min_current = current
        min_res_index = i + 1
print(f"Сопротивление с минимальным током: №{min_res_index}")
