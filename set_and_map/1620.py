import sys
input = sys.stdin.readline

def is_number(n):
    try:
        int(n)
        return True
    except:
        return False
    
n, m = map(int, input().split())
poketmons = {}
poketmons_reverse = {}
for i in range(1, n+1):
    poketmon = input().strip()
    poketmons[i] = poketmon
    poketmons_reverse[poketmon] = i

for i in range(m):
    q = input().strip()
    if is_number(q):
        print(poketmons.get(int(q)))
    else:
        print(poketmons_reverse.get(q))