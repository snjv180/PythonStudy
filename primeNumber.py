from math import sqrt
n = 100
sqrt_n = int(sqrt(n))
no_primes = {j for i in range(2,sqrt_n) for j in range(i*2, n, i)}
primes = {i for i in range(n) if i not in no_primes}
print(primes)