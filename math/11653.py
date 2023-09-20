import sys
print = sys.stdout.write

primes = [2, 3]
def is_prime(num):
    if num == 1: return False
    if num in primes: return True
    
    for prime in primes:
        if num % prime == 0:
            return False
    primes.append(num)
    return is_prime

n = int(input())
quotient = n
for i in range(2, n+1):
    if quotient == 1: break
    if is_prime(i):
        prime = i
        while quotient % prime == 0:
            print(f'{prime}\n')
            quotient //= prime