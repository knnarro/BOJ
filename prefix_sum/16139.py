import sys
input = sys.stdin.readline
print = sys.stdout.write

word = input().strip()
q = int(input())
sums = [{word[0]:1}]
for i in range(1, len(word)):
    char = word[i]
    count = sums[i-1].copy()
    count[word[i]] = count.get(word[i], 0) + 1
    sums.append(count)

for _ in range(q):
    char, start, end = input().split()
    start, end = int(start), int(end)
    if start == 0:
        print(f'{sums[end].get(char, 0)}\n')
    else:
        print(f'{sums[end].get(char, 0) - sums[start-1].get(char, 0)}\n')