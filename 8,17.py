num_prev2, den_prev2 = 1, 1 
num_prev1, den_prev1 = 2, 1 
print(f"a1 = {num_prev2}/{den_prev2} = {num_prev2/den_prev2:.5f}")
print(f"a2 = {num_prev1}/{den_prev1} = {num_prev1/den_prev1:.5f}")
n = 3
while True:
    num = num_prev1 + num_prev2
    den = den_prev1 + den_prev2
    value = num / den
    prev_value = num_prev1 / den_prev1
    diff = abs(value - prev_value)
    print(f"a{n} = {num}/{den} = {value:.5f}, разница с предыдущим: {diff:.5f}")
    if diff <= 0.001:
        print(f"Первый член, отличающийся от предыдущего не более чем на 0.001: a{n} = {value:.5f}")
        break
    num_prev2, den_prev2 = num_prev1, den_prev1
    num_prev1, den_prev1 = num, den
    n += 1
