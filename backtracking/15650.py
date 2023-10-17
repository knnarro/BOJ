import sys
input = sys.stdin.readline

n, m = map(int, input().split())
visited = []

def dfs(depth, start):
    if depth > m:
        print(*visited)
        return 
    
    for number in range(start, n+1):
        if not number in visited:
            visited.append(number)
            dfs(depth+1, number)
            visited.pop()

dfs(1, 1)