import sys
print = sys.stdout.write

n = int(input())
quotient = n
for i in range(2, n+1):
    if quotient == 1: break
    while quotient % i == 0:
        print(f'{i}\n')
        quotient //= i