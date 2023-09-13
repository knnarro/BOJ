import sys
input = sys.stdin.readline
print = sys.stdout.write

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(f'{a+b}\n')