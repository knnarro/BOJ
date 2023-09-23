import sys
from math import sqrt, floor
input = sys.stdin.readline
print = sys.stdout.write

def get_prime_gte_n(n):
    num = max(n, 2) # 2미만의 n은 2로 취급
    while True:
        is_prime = True
        for divisor in range(2, floor(sqrt(num))+1):
            if num % divisor == 0:
                is_prime = False
                break;
        if is_prime: return num
        num += 1

t = int(input())
for i in range(t):
    n = int(input())
    print(f'{get_prime_gte_n(n)}\n')