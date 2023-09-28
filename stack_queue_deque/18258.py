import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
q = deque()
for i in range(n):
    command = list(input().split())
    if command[0] == 'push':
        q.append(command[1])
    elif command[0] == 'pop':
        if len(q) == 0:
            print('-1\n')
        else: 
            print(f'{q.popleft()}\n')
    elif command[0] == 'size':
        print(f'{len(q)}\n')
    elif command[0] == 'empty':
        if len(q) == 0:
            print('1\n')
        else:
            print('0\n')
    elif command[0] == 'front':
        if len(q) == 0:
            print('-1\n')
        else:
            front = q.popleft()
            q.appendleft(front)
            print(f'{front}\n')
    elif command[0] == 'back':
        if len(q) == 0:
            print('-1\n')
        else:
            back = q.pop()
            q.append(back)
            print(f'{back}\n')