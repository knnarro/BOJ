import sys
input = sys.stdin.readline

n, m = map(int, input().split())
temperatures = list(map(int, input().split()))
sums = [sum(temperatures[0:m])]
for i in range(1, n-m+1):
    sums.append(sums[i-1]-temperatures[i-1]+temperatures[i+m-1])

print(max(sums))