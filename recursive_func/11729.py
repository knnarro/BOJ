import sys
print = sys.stdout.write

results = []
def hanoi(n, start, end):
    if n == 0:
        return
    next = 6 - start - end
    hanoi(n-1, start, next)
    results.append((start, end))
    hanoi(n-1, next, end)

n = int(input())
hanoi(n, 1, 3)
print(f'{len(results)}\n')
for result in results:
    print(f'{result[0]} {result[1]}\n')