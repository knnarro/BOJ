import sys
input = sys.stdin.readline

n, m = input().split()
a = set(map(int, input().split()))
b = set(map(int, input().split()))

count = len(a) + len(b) - 2*len(a.intersection(b))
print(count)