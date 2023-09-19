import sys
input = sys.stdin.readline
print = sys.stdout.write

t = int(input())
coins = [25, 10, 5, 1]
for i in range(t):
    c = int(input())
    remainder = c
    for coin in coins:
        quotient = remainder // coin
        remainder %= coin
        print(f'{quotient} ')
    print('\n')