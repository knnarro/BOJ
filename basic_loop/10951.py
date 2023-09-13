import sys
print = sys.stdout.write

lines = sys.stdin.readlines()
for line in lines:
    a, b = map(int, line.split())
    print(f'{a+b}\n')