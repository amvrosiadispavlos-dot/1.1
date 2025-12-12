def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

primes = []
num = 100
while len(primes) < 10:
    if is_prime(num):
        primes.append(num)
    num += 1
print("Первые 10 простых чисел, начиная с 100:", primes)
