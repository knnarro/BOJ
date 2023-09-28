import sys
input = sys.stdin.readline
print = sys.stdout.write

m = int(input())
s = [0] * 21
for i in range(m):
    command = list(input().split())
    if command[0] == 'add':
        s[int(command[1])] = 1
    elif command[0] == 'remove':
        s[int(command[1])] = 0
    elif command[0] == 'check':
        print(f'{s[int(command[1])]}\n')
    elif command[0] == 'toggle':
        if s[int(command[1])] == 1:
            s[int(command[1])] = 0
        else:
            s[int(command[1])] = 1
    elif command[0] == 'all':
        s = [1 for _ in range(0, 21)]
    else:
        s = [0 for _ in range(0, 21)]