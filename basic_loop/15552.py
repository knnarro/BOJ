import sys
input = sys.stdin.readline
print = sys.stdout.write

t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print(f'{a+b}\n')