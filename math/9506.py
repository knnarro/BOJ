import sys
from math import sqrt, floor

input = sys.stdin.readline
print = sys.stdout.write

while True:
    n = int(input())
    if n == -1: break

    factors = []
    for i in range(2, floor(sqrt(n))+1):
        if n % i == 0:
            factors.append(i)
            if i != n//i: 
                factors.append(n//i)

    if sum(factors)+1 == n:
        factors.sort()
        print(f'{n} = 1')
        for factor in factors:
            print(f' + {factor}')
        print('\n')
    else:
        print(f'{n} is NOT perfect.\n')