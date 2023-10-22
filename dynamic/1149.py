import sys
input = sys.stdin.readline

n = int(input())
cost = [{'r': 0, 'g':0, 'b':0} for _ in range(n+1)]
for i in range(1, n+1):
    r, g, b = map(int, input().split())
    cost[i]['r'] = min(cost[i-1]['g'], cost[i-1]['b']) + r
    cost[i]['g'] = min(cost[i-1]['r'], cost[i-1]['b']) + g
    cost[i]['b'] = min(cost[i-1]['r'], cost[i-1]['g']) + b

print(min(cost[n].values()))