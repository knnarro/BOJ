n = int(input())
line = list(map(int, input().split()))
line.reverse()
waiting = []

for current_order in range(1, n+1):
    if len(line) > 0 and line[-1] == current_order:
        line.pop()
        continue
    elif len(waiting) > 0 and waiting[-1] == current_order:
        waiting.pop()
        continue
    while len(line) > 0:
        order = line.pop()
        if order == current_order:
            break
        else:
            waiting.append(order)

if len(waiting) > 0:
    print('Sad')
else:
    print('Nice')