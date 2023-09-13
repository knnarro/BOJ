h, m = map(int, input().split())
ans_h = h
ans_m = m-45

if ans_m < 0:
    ans_m += 60
    ans_h -= 1
if ans_h < 0:
    ans_h = 23

print(f'{ans_h} {ans_m}')