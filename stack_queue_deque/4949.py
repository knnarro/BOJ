import sys
input = sys.stdin.readline
print = sys.stdout.write

while True:
    str = input().rstrip()
    if str == '.':
        break
    stack = []
    is_vps = 'yes'
    for char in str:
        try:
            if char in ['(', '[']:
                stack.append(char)
            elif char == ')' and stack.pop() != '(':
                raise Exception
            elif char == ']' and stack.pop() != '[':
                raise Exception
        except:
            is_vps = 'no'
            break

    if len(stack) > 0:
        is_vps = 'no'
    print(f'{is_vps}\n')