import sys
from functools import cmp_to_key
input = sys.stdin.readline
print = sys.stdout.write

def compare_word(prev, cur):
    if len(prev) > len(cur):
        return 1
    elif len(prev) < len(cur):
        return -1
    else:
        if prev > cur:
            return 1
        if prev == cur:
            return 0
        else:
            return -1

n = int(input())
words = set()
for i in range(n):
    words.add(input())
words = list(words)

words.sort(key=cmp_to_key(compare_word))
for word in words:
    print(f'{word}')