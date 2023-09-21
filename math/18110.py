import sys
from math import floor, ceil
input = sys.stdin.readline

def round(num):
    if num - int(num) >= 0.5:
        return ceil(num)
    else:
        return floor(num)

scores = []
n = int(input())
for i in range(n):
    scores.append(int(input()))

if scores == []:
    print(0)
else:
    scores.sort()
    cut_off = round(n * 0.15)
    scores = scores[cut_off:-cut_off] if cut_off > 0 else scores
    avg = round(sum(scores)/len(scores))
    print(avg)