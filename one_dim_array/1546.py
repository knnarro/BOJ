import sys
input = sys.stdin.readline

n = int(input())
scores = list(map(int, input().split()))
max = max(scores)
sum = sum(scores)
avg = (sum/n) * (100/max)
print(avg)