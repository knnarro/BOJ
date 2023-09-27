import sys
input = sys.stdin.readline
print = sys.stdout.write

t = int(input())
for i in range(t):
    stack = []
    str = input().strip()
    is_vps = 'YES'
    for char in str:
        if char == '(':
            stack.append(char)
        else:
            try:
                stack.pop()
            except:
                is_vps = 'NO'
                break
    if len(stack) != 0:
        is_vps = 'NO'
    print(f'{is_vps}\n')