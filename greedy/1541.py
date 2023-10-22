expression = input()
ans = 0
has_been_minus_appeared = False

num = ''
for char in expression:
    if char in ['+', '-']:
        if has_been_minus_appeared:
            ans -= int(num)
        else:
            ans += int(num)
        if char == '-':
            has_been_minus_appeared = True
        num = ''
    else:
        num += char

if has_been_minus_appeared:
    ans -= int(num)
else:
    ans += int(num)
    
print(ans)