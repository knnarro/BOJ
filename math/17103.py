import sys
from math import sqrt, floor, ceil
input = sys.stdin.readline
print = sys.stdout.write

def get_prime_list(n):
    primes = [True] * (n+1)
    for i in range(2, floor(sqrt(n))+1):
        if primes[i] == True:
            for j in range(i+i, n+1, i):
                primes[j] = False
    return primes

def round(n):
    if n - int(n) < 0.5:
        return floor(n)
    else:
        return ceil(n)

def execute():
    t = int(input())
    inputs = []
    for i in range(t):
        inputs.append(int(input()))
    primes = get_prime_list(max(inputs))

    for num in inputs:
        count = 0
        for i in range(2, num//2 + 1):
            if primes[i] and primes[num-i]:
                count += 1
        print(f'{count}\n')

execute()