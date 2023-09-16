import sys
input = sys.stdin.readline
print = sys.stdout.write

remainders = []
for i in range(10):
    n = int(input())
    r = n % 42
    if not r in remainders:
        remainders.append(r)
 
count = len(remainders)
print(f'{count}')