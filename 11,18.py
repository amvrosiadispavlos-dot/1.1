# а) Числа, делящиеся на 13 или 17, начиная с 300
result_a = []
num = 300
while len(result_a) < 20:
    if num % 13 == 0 or num % 17 == 0:
        result_a.append(num)
    num += 1
print("а) 20 чисел, делящихся на 13 или 17 от 300:", result_a)

# б) Первые 30 простых чисел
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

result_b = []
num = 2
while len(result_b) < 30:
    if is_prime(num):
        result_b.append(num)
    num += 1
print("б) Первые 30 простых чисел:", result_b)
