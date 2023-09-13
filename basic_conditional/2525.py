cur_h, cur_m = map(int, input().split())
taken_time = int(input())
taken_h = taken_time // 60
taken_m = taken_time % 60

ans_h = cur_h + taken_h
ans_m = cur_m + taken_m

if ans_m >= 60:
    ans_m -= 60
    ans_h += 1
ans_h %= 24

print(f'{ans_h} {ans_m}')