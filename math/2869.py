a, b, v = map(int, input().split())
v = v-a # 마지막날은 내려가지 않음
day = v//(a-b)
has_remainder = v%(a-b) > 0
print(day+2 if has_remainder else day+1)