fib = [1, 1]
for i in range(2, 10):
    fib.append(fib[i-1] + fib[i-2])
for i in range(2, 10):
    print(f"{i+1}-й член: {fib[i]}")
