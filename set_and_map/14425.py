import sys
input = sys.stdin.readline

n, m = map(int, input().split())
words = set()
for i in range(n):
    words.add(input())

count = 0
for i in range(m):
    word = input()
    if word in words:
        count += 1

print(count)