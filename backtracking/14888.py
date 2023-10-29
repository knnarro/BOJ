import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
ops_count = list(map(int, input().split()))
max_value = -1e10
min_value = 1e10

def dfs(depth, value, plus, minus, multiple, divide):
    global max_value, min_value
    if depth >= n:
        if max_value < value:
            max_value = value
        if min_value > value:
            min_value = value
    if plus > 0:
        dfs(depth+1, value+numbers[depth], plus-1, minus, multiple, divide)
    if minus > 0:
        dfs(depth+1, value-numbers[depth], plus, minus-1, multiple, divide)
    if multiple > 0:
        dfs(depth+1, value*numbers[depth], plus, minus, multiple-1, divide)
    if divide > 0:
        dfs(depth+1, int(value/numbers[depth]), plus, minus, multiple, divide-1)

dfs(1, numbers[0], ops_count[0], ops_count[1], ops_count[2], ops_count[3])
print(max_value)
print(min_value)