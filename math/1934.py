import sys
input = sys.stdin.readline
print = sys.stdout.write

def get_lcm(x:int, y:int):
    gcd = 1
    for d in range(min(x, y), 0, -1):
        if x % d == 0 and y % d == 0:
            gcd = d
            break
    lcm = x * y / gcd
    return int(lcm)
    
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    lcm = get_lcm(a, b)
    print(f'{lcm}\n')