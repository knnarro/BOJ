n, m = map(int, input().split())
numbers = [i for i in range(1, n+1)]
visited = []

def dfs(depth):
    if depth > m:
        print(*visited)
        return
    
    for number in numbers:
        visited.append(number)
        dfs(depth+1)
        visited.pop()

dfs(1)