import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
deq = deque()

for i in range(n):
    command = list(map(int, input().split()))
    try:
        if command[0] == 1:
            deq.appendleft(command[1])
        elif command[0] == 2:
            deq.append(command[1])
        elif command[0] == 3:
            print(f'{deq.popleft()}\n')
        elif command[0] == 4:
            print(f'{deq.pop()}\n')
        elif command[0] == 5:
            print(f'{len(deq)}\n')
        elif command[0] == 6:
            print(f'{1 if len(deq) == 0 else 0}\n')
        elif command[0] == 7:
            front = deq.popleft()
            deq.appendleft(front)
            print(f'{front}\n')
        else:
            back = deq.pop()
            deq.append(back)
            print(f'{back}\n')
    except:
        print(f'-1\n')