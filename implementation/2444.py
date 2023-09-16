import sys
print = sys.stdout.write

n = int(input())
# 윗부분
for i in range(1, n+1):
    for space in range(n-i):
        print(' ')
    for star in range(2*i-1):
        print('*')
    print('\n')
# 아랫부분
for i in range(1, n):
    for space in range(i):
        print(' ')
    for star in range(2*(n-i)-1):
        print('*')
    print('\n')