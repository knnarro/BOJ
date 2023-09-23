import sys
from math import sqrt, floor
input = sys.stdin.readline
print = sys.stdout.write

def get_prime_list(n):
    primes = [True] * (n+1)
    for i in range(2, floor(sqrt(n))+1):
        if primes[i] == True:
            for j in range(i+i, n+1, i):
                primes[j] = False
    return [ i for i in range(2, n+1) if primes[i] == True ]

inputs = []
while True:
    n = int(input())
    if n == 0:
        break
    inputs.append(n)
    
max = max(inputs)
primes = get_prime_list(2*max)

for num in inputs:
    primes_in_range = list(filter(lambda prime: prime > num and prime <= 2*num, primes))
    print(f'{len(primes_in_range)}\n')