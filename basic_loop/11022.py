import sys
input = sys.stdin.readline
print = sys.stdout.write

t = int(input())
for i in range(1, t+1):
    a, b = map(int, input().split())
    print(f'Case #{i}: {a} + {b} = {a+b}\n')