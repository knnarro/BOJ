import sys
input = sys.stdin.readline
print= sys.stdout.write

def cantor(num):
    if num == 0:
        print('-')
        return
    cantor(num-1)
    for _ in range(3**(num-1)):
        print(' ')
    cantor(num-1)

while True:
    try:
        n = int(input())
        cantor(n)
        print('\n')
    except:
        break