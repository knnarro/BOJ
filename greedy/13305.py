import sys
input = sys.stdin.readline

n = int(input())
distances = list(map(int, input().split()))
costs = list(map(int, input().split()))

min_cost = costs[0]
sum_distance = 0
ans = 0
for i in range(n-1):
    if min_cost <= costs[i]:
        sum_distance += distances[i]
    else:
        ans += min_cost * sum_distance
        min_cost = costs[i]
        sum_distance = distances[i]
ans += min_cost * sum_distance

print(ans)