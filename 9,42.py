for d1 in range(1, 10):
    for d2 in range(10):
        for d3 in range(10):
            if d1 != d2 and d1 != d3 and d2 != d3:
                print(d1*100 + d2*10 + d3)
