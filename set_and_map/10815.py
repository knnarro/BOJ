import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
cards = set(map(int, input().split()))
m = int(input())
numbers = list(map(int, input().split()))

for number in numbers:
    if number in cards:
        print('1 ')
    else:
        print('0 ')