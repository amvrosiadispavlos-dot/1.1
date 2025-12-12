def insert_before_multiples(arr, num, a):
    result = []
    for x in arr:
        if x % a == 0:
            result.append(num)
        result.append(x)
    return result
def insert_after_negatives(arr, num):
    result = []
    for x in arr:
        result.append(x)
        if x < 0:
            result.append(num)
    return result
