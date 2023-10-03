import sys
input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())
vocas = {}
for _ in range(n):
    word = input().strip()
    if len(word) >= m:
        count = vocas.get(word, 0)
        vocas[word] = count + 1

vocas = list(sorted(vocas.items(), key=lambda item: (-item[1], -len(item[0]), item[0])))
for voca in vocas:
    print(f'{voca[0]}\n')