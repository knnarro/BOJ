import sys
from math import sqrt, floor

print = sys.stdout.write

def is_prime(num):
    if num == 1: return False
    if num == 2: return True
    sq_root = floor(sqrt(num))
    for i in range(2, sq_root+1):
        if num % i == 0:
            return False
    return True

m, n = map(int, input().split())
for i in range(m, n+1):
    if is_prime(i):
        print(f'{i}\n')