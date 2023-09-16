import sys
input = sys.stdin.readline
print = sys.stdout.write

t = int(input())
for i in range(t):
    r, s = input().split()
    for char in s:
        for j in range(int(r)):
            print(f'{char}')
    print('\n')