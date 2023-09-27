import sys
from queue import LifoQueue
input = sys.stdin.readline

stack = LifoQueue()
n = int(input())
for i in range(n):
    command = list(map(int, input().split()))
    if command[0] == 1:
        stack.put_nowait(command[1])
    elif command[0] == 2:
        try:
            top = stack.get_nowait()
            print(top)
        except:
            print(-1)
    elif command[0] == 3:
        print(stack.qsize())
    elif command[0] == 4:
        if stack.empty():
            print(1)
        else:
            print(0)
    else:
        try:
            top = stack.get_nowait()
            print(top)
            stack.put(top)
        except:
            print(-1)