import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
for i in range(1, n+1):
    for space in range(n-i):
        print(' ')
    for star in range(i):
        print('*')
    print('\n')